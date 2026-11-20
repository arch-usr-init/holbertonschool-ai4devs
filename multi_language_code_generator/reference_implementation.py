import json
import re
from collections import Counter

def analyze_logs(log_data: str) -> str:
    if not log_data or not log_data.strip():
        return json.dumps({"total_requests": 0, "unique_visitors": 0, "error_rate": 0.0, "top_url": None})
    lines = log_data.strip().split('\n')
    total_requests, error_count, unique_ips, url_counts = 0, 0, set(), Counter()
    log_pattern = re.compile(r'^(?P<ip>\S+) \S+ \S+ \[.*?\] "(?P<method>\S+) (?P<url>\S+) \S+" (?P<status>\d{3}) \S+$')
    
    for line in lines:
        match = log_pattern.match(line)
        if match:
            total_requests += 1
            unique_ips.add(match.group('ip'))
            status = int(match.group('status'))
            if 400 <= status <= 599:
                error_count += 1
            url_counts[match.group('url')] += 1

    error_rate = round((error_count / total_requests) * 100, 2) if total_requests > 0 else 0.0
    top_url = url_counts.most_common(1)[0][0] if url_counts else None
    return json.dumps({"total_requests": total_requests, "unique_visitors": len(unique_ips), "error_rate": error_rate, "top_url": top_url}, indent=4)
