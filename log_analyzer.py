class LogAnalyzer:
    def parse_line(self, line: str) -> dict:
        parts = line.split('"')
        if len(parts) < 2:
            return None
        request_info = parts[1].split()
        if len(request_info) < 2:
            return None
        url = request_info[1]
        
        # Status code is usually right after the quotes
        status_part = parts[2].strip().split()
        if not status_part:
            return None
        status = int(status_part[0])
        
        ip = line.split()[0]
        return {"ip": ip, "url": url, "status": status}

    def analyze(self, lines: list) -> dict:
        if not lines:
            return {"total_requests": 0, "unique_visitors": 0, "error_rate": 0.0, "top_url": None}
        
        parsed_lines = [self.parse_line(l) for l in lines if self.parse_line(l)]
        if not parsed_lines:
            return {"total_requests": 0, "unique_visitors": 0, "error_rate": 0.0, "top_url": None}

        total = len(parsed_lines)
        errors = sum(1 for l in parsed_lines if l["status"] >= 400)
        unique_ips = len(set(l["ip"] for l in parsed_lines))
        
        urls = {}
        for l in parsed_lines:
            urls[l["url"]] = urls.get(l["url"], 0) + 1
        top_url = max(urls, key=urls.get) if urls else None

        return {
            "total_requests": total,
            "unique_visitors": unique_ips,
            "error_rate": round((errors / total) * 100, 2),
            "top_url": top_url
        }
