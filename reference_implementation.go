package main
import ("encoding/json";"fmt";"regexp";"strconv";"strings")
type LogStats struct { TotalRequests int `json:"total_requests"`; UniqueVisitors int `json:"unique_visitors"`; ErrorRate float64 `json:"error_rate"`; TopURL *string `json:"top_url"` }
func analyzeLogs(logData string) string {
	stats := LogStats{TotalRequests: 0, UniqueVisitors: 0, ErrorRate: 0.0, TopURL: nil}
	if strings.TrimSpace(logData) == "" { b, _ := json.MarshalIndent(stats, "", "    "); return string(b) }
	lines := strings.Split(strings.TrimSpace(logData), "\n"); uniqueIps := make(map[string]bool); urlCounts := make(map[string]int); errorCount := 0
	logPattern := regexp.MustCompile(`^(\S+) \S+ \S+ \[.*?\] "\S+ (\S+) \S+" (\d{3}) \S+$`)
	for _, line := range lines {
		matches := logPattern.FindStringSubmatch(line)
		if len(matches) == 4 {
			stats.TotalRequests++; uniqueIps[matches[1]] = true; url := matches[2]; status, _ := strconv.Atoi(matches[3])
			if status >= 400 && status <= 599 { errorCount++ }; urlCounts[url]++
		}
	}
	stats.UniqueVisitors = len(uniqueIps)
	if stats.TotalRequests > 0 { rate := (float64(errorCount) / float64(stats.TotalRequests)) * 100; stats.ErrorRate = float64(int(rate*100+0.5)) / 100 }
	maxCount := 0; for url, count := range urlCounts { if count > maxCount { maxCount = count; u := url; stats.TopURL = &u } }
	b, _ := json.MarshalIndent(stats, "", "    "); return string(b)
}
func main() { fmt.Println(analyzeLogs(`192.168.1.1 - - [10/Oct/2023:13:55:36 -0700] "GET /index.html HTTP/1.1" 200 2326`)) }
