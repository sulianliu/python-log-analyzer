from datetime import datetime

from analyzer.model import LogEntry
from analyzer.rules_service_error_count import ServiceErrorCountRule


def test_service_error_count_for_specific_service():
    entries = [
        LogEntry(datetime.now(), "ERROR", "e1", "auth"),
        LogEntry(datetime.now(), "ERROR", "e2", "auth"),
        LogEntry(datetime.now(), "ERROR", "e3", "order"),
    ]

    rule = ServiceErrorCountRule(threshold=2, service="auth")
    results = rule.analyze(entries)

    assert len(results) == 1
    assert "auth" in results[0].detail


def test_service_error_count_all_services():
    entries = [
        LogEntry(datetime.now(), "ERROR", "e1", "auth"),
        LogEntry(datetime.now(), "ERROR", "e2", "order"),
    ]

    rule = ServiceErrorCountRule(threshold=1)
    results = rule.analyze(entries)

    assert len(results) == 2
