# Cross-Language Specification - Log Analyzer

## Algorithm
Parse standard Apache/Nginx access logs and compute basic traffic statistics:
1. Total number of requests.
2. Number of unique visitors (based on unique IP addresses).
3. Error rate (percentage of HTTP status codes 400-599).
4. The most frequently requested URL.

## Inputs
- A multi-line string or text file where each line represents a single HTTP request in Common Log Format:
  `IP - - [Timestamp] "HTTP_METHOD URL PROTOCOL" STATUS_CODE BYTES`

## Outputs
- A JSON object (or dictionary) with the following keys:
  - `total_requests` (Integer)
  - `unique_visitors` (Integer)
  - `error_rate` (Float, rounded to 2 decimal places)
  - `top_url` (String)

## Edge Cases
- **Empty input**: If the file is empty, return total_requests=0, unique_visitors=0, error_rate=0.0, top_url=None.
- **Malformed lines**: Skip lines that do not match the Common Log Format.
- **No errors**: If there are 0 error codes, the error_rate must be 0.0 (avoid division by zero).
- **All errors**: If every request is an error, the error_rate must be 100.0.
- **Tie for top URL**: If multiple URLs have the same highest frequency, return the one that appeared first.

## Test Cases
1. **Empty File**:
   - Input: `""`
   - Expected Output: `{"total_requests": 0, "unique_visitors": 0, "error_rate": 0.0, "top_url": null}`
2. **Single Valid Request**:
   - Input: `192.168.1.1 - - [10/Oct/2023:13:55:36 -0700] "GET /index.html HTTP/1.1" 200 2326`
   - Expected Output: `{"total_requests": 1, "unique_visitors": 1, "error_rate": 0.0, "top_url": "/index.html"}`
3. **Multiple Requests, No Errors**:
   - Input: 3 lines, all with status 200, from 2 different IPs, requesting `/home` twice and `/about` once.
   - Expected Output: `{"total_requests": 3, "unique_visitors": 2, "error_rate": 0.0, "top_url": "/home"}`
4. **Mixed Requests with Errors**:
   - Input: 4 lines. 2 lines with status 200, 2 lines with status 404/500.
   - Expected Output: `{"total_requests": 4, ..., "error_rate": 50.0, ...}`
5. **Malformed and Valid Lines Mixed**:
   - Input: 2 valid lines, 1 line of random text (e.g., `"This is not a log"`).
   - Expected Output: The script must ignore the malformed line and calculate stats based only on the 2 valid lines (total_requests = 2).
