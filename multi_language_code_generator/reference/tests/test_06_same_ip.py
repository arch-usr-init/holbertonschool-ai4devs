from log_analyzer import LogAnalyzer
def test_same_ip():
    lines = ['1.1.1.1 - - [10/Oct] "GET / HTTP/1.1" 200 1', '1.1.1.1 - - [10/Oct] "GET / HTTP/1.1" 200 1']
    assert LogAnalyzer().analyze(lines)["unique_visitors"] == 1
