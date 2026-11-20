from log_analyzer import LogAnalyzer
def test_mixed():
    lines = ['1.1.1.1 - - [10/Oct] "GET /a HTTP/1.1" 200 1', '1.1.1.1 - - [10/Oct] "GET /b HTTP/1.1" 500 1']
    assert LogAnalyzer().analyze(lines)["error_rate"] == 50.0
