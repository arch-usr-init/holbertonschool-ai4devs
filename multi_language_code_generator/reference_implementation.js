function analyzeLogs(logData) {
    if (!logData || !logData.trim()) {
        return JSON.stringify({
            total_requests: 0,
            unique_visitors: 0,
            error_rate: 0.0,
            top_url: null
        }, null, 4);
    }

    const lines = logData.trim().split('\n');
    let totalRequests = 0;
    let errorCount = 0;
    const uniqueIps = new Set();
    const urlCounts = new Map();

    const logPattern = /^(\S+) \S+ \S+ \[.*?\] "\S+ (\S+) \S+" (\d{3}) \S+$/;

    for (const line of lines) {
        const match = line.match(logPattern);
        if (match) {
            totalRequests++;
            uniqueIps.add(match[1]);
            const status = parseInt(match[3], 10);
            const url = match[2];

            if (status >= 400 && status <= 599) {
                errorCount++;
            }
            
            urlCounts.set(url, (urlCounts.get(url) || 0) + 1);
        }
    }

    const errorRate = totalRequests > 0 ? parseFloat(((errorCount / totalRequests) * 100).toFixed(2)) : 0.0;
    
    let topUrl = null;
    let maxCount = 0;
    for (const [url, count] of urlCounts.entries()) {
        if (count > maxCount) {
            maxCount = count;
            topUrl = url;
        }
    }

    return JSON.stringify({
        total_requests: totalRequests,
        unique_visitors: uniqueIps.size,
        error_rate: errorRate,
        top_url: topUrl
    }, null, 4);
}

// Test
const sampleLog = '192.168.1.1 - - [10/Oct/2023:13:55:36 -0700] "GET /index.html HTTP/1.1" 200 2326';
console.log(analyzeLogs(sampleLog));
