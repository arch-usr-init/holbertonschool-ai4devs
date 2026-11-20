from ..log_analyzer import LogAnalyzer
def test_malformed(): assert LogAnalyzer().analyze(["invalid", "text"])["total_requests"] == 0
