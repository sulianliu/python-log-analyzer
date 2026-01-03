from datetime import datetime

from analyzer.model import LogEvent
from analyzer.stats import top_services


def test_top_services_counts_correctly():
    events = [
        LogEvent(datetime.now(), "ERROR", "OrderService", "err1"),
        LogEvent(datetime.now(), "ERROR", "OrderService", "err2"),
        LogEvent(datetime.now(), "WARN", "AuthService", "warn"),
    ]

    result = top_services(events, level="ERROR", top_n=5)

    assert result == [("OrderService", 2)]
