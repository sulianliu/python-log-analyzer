from analyzer.model import LogEntry
from analyzer.rules_error_count import ErrorCountRule


def test_error_count_rule_triggers_when_threshold_met():
    entries = [
        LogEntry("t", "ERROR", "e1"),
        LogEntry("t", "ERROR", "e2"),
    ]

    rule = ErrorCountRule(threshold=2)
    results = rule.analyze(entries)

    assert len(results) == 1


def test_error_count_rule_not_triggered_when_below_threshold():
    entries = [
        LogEntry("t", "ERROR", "e1"),
    ]

    rule = ErrorCountRule(threshold=2)
    results = rule.analyze(entries)

    assert results == []
