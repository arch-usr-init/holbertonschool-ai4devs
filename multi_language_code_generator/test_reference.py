import pytest
from reference_implementation import analyze_logs
import json

def test_empty_input():
    result = json.loads(analyze_logs(""))
    assert result["total_requests"] == 0
    assert result["top_url"] is None

def test_single_valid_request():
    log = '192.168.1.1 - - [10/Oct/2023:13:55:36 -0700] "GET /index.html HTTP/1.1" 200 2326'
    result = json.loads(analyze_logs(log))
    assert result["total_requests"] == 1
    assert result["unique_visitors"] == 1
    assert result["error_rate"] == 0.0
    assert result["top_url"] == "/index.html"

def test_mixed_errors_and_ties():
    log = """192.168.1.1 - - [10/Oct/2023:13:55:36 -0700] "GET /home HTTP/1.1" 200 2326
192.168.1.2 - - [10/Oct/2023:13:55:37 -0700] "GET /home HTTP/1.1" 200 2326
192.168.1.1 - - [10/Oct/2023:13:55:38 -0700] "GET /about HTTP/1.1" 404 2326
192.168.1.3 - - [10/Oct/2023:13:55:39 -0700] "GET /contact HTTP/1.1" 500 2326
Invalid Line Here"""
    result = json.loads(analyze_logs(log))
    assert result["total_requests"] == 4
    assert result["unique_visitors"] == 3
    assert result["error_rate"] == 50.0
    assert result["top_url"] == "/home"
