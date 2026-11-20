import pytest
from ..log_analyzer import LogAnalyzer

analyzer = LogAnalyzer()

def test_empty_list():
    assert analyzer.analyze([]) == {"total_requests": 0, "unique_visitors": 0, "error_rate": 0.0, "top_url": None}

def test_malformed_lines():
    lines = ["Invalid log line", "Another invalid"]
    assert analyzer.analyze(lines)["total_requests"] == 0

def test_single_200_request():
    lines = ['192.168.1.1 - - [10/Oct/2023] "GET /index.html HTTP/1.1" 200 2326']
    res = analyzer.analyze(lines)
    assert res["total_requests"] == 1
    assert res["error_rate"] == 0.0
    assert res["top_url"] == "/index.html"

def test_single_404_request():
    lines = ['192.168.1.1 - - [10/Oct/2023] "GET /missing HTTP/1.1" 404 2326']
    res = analyzer.analyze(lines)
    assert res["error_rate"] == 100.0

def test_multiple_unique_ips():
    lines = [
        '192.168.1.1 - - [10/Oct/2023] "GET /a HTTP/1.1" 200 2326',
        '192.168.1.2 - - [10/Oct/2023] "GET /b HTTP/1.1" 200 2326'
    ]
    assert analyzer.analyze(lines)["unique_visitors"] == 2

def test_same_ip_multiple_requests():
    lines = [
        '192.168.1.1 - - [10/Oct/2023] "GET /a HTTP/1.1" 200 2326',
        '192.168.1.1 - - [10/Oct/2023] "GET /b HTTP/1.1" 200 2326'
    ]
    assert analyzer.analyze(lines)["unique_visitors"] == 1

def test_top_url():
    lines = [
        '192.168.1.1 - - [10/Oct/2023] "GET /home HTTP/1.1" 200 2326',
        '192.168.1.2 - - [10/Oct/2023] "GET /home HTTP/1.1" 200 2326',
        '192.168.1.3 - - [10/Oct/2023] "GET /about HTTP/1.1" 200 2326'
    ]
    assert analyzer.analyze(lines)["top_url"] == "/home"

def test_mixed_errors():
    lines = [
        '192.168.1.1 - - [10/Oct/2023] "GET /a HTTP/1.1" 200 2326',
        '192.168.1.2 - - [10/Oct/2023] "GET /b HTTP/1.1" 500 2326'
    ]
    assert analyzer.analyze(lines)["error_rate"] == 50.0

def test_all_errors():
    lines = [
        '192.168.1.1 - - [10/Oct/2023] "GET /a HTTP/1.1" 400 2326',
        '192.168.1.2 - - [10/Oct/2023] "GET /b HTTP/1.1" 500 2326'
    ]
    assert analyzer.analyze(lines)["error_rate"] == 100.0

def test_parse_line_directly():
    line = '192.168.1.1 - - [10/Oct/2023] "GET /test HTTP/1.1" 201 1234'
    parsed = analyzer.parse_line(line)
    assert parsed["status"] == 201
    assert parsed["url"] == "/test"
