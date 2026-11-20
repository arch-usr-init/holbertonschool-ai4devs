from log_analyzer import LogAnalyzer
def test_empty(): assert LogAnalyzer().analyze([])["total_requests"] == 0
