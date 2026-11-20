from ..log_analyzer import LogAnalyzer
def test_error(): assert LogAnalyzer().analyze(['1.1.1.1 - - [10/Oct] "GET / HTTP/1.1" 404 1'])["error_rate"] == 100.0
