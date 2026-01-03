from datetime import datetime

from analyzer.model import LogEntry
from analyzer.parser import parse_lines


def test_parse_new_format_with_service():
    lines = [
        "2025-01-01T10:00:00 auth-service ERROR boom"
    ]

    entries = parse_lines(lines)

    assert entries == [
        LogEntry(
            timestamp=datetime(2025, 1, 1, 10, 0, 0),
            service="auth-service",
            level="ERROR",
            message="boom",
        )
    ]


def test_parse_old_format_without_service():
    lines = [
        "2025-01-01T10:00:00 ERROR boom"
    ]

    entries = parse_lines(lines)

    assert entries[0].service is None
