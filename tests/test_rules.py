from analyzer.model import LogEntry, AnalysisResult
from analyzer.rules import ErrorRule


def test_error_rule_detects_error():
    entries = [
        LogEntry("t1", "INFO", "ok"),
        LogEntry("t2", "ERROR", "boom"),
    ]

    rule = ErrorRule()
    results = rule.analyze(entries)

    assert results == [
        AnalysisResult(
            rule="error-detection",
            detail="boom",
            line=2,
        )
    ]
