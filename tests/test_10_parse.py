from ..log_analyzer import LogAnalyzer
def test_parse():
    res = LogAnalyzer().parse_line('1.1.1.1 - - [10/Oct] "GET /test HTTP/1.1" 201 1')
    assert res["status"] == 201 and res["url"] == "/test"
