from ..log_analyzer import LogAnalyzer
def test_single(): assert LogAnalyzer().analyze(['1.1.1.1 - - [10/Oct] "GET / HTTP/1.1" 200 1'])["total_requests"] == 1
