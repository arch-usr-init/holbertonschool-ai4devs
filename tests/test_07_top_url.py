from ..log_analyzer import LogAnalyzer
def test_top_url():
    lines = ['1.1.1.1 - - [10/Oct] "GET /a HTTP/1.1" 200 1', '1.1.1.1 - - [10/Oct] "GET /a HTTP/1.1" 200 1', '1.1.1.1 - - [10/Oct] "GET /b HTTP/1.1" 200 1']
    assert LogAnalyzer().analyze(lines)["top_url"] == "/a"
