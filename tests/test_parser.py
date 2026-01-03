from analyzer.parser import parse_line


def test_parse_valid_log_line():
    line = "2025-01-01 10:01:05 ERROR OrderService Failed to create order"
    event = parse_line(line)

    assert event is not None
    assert event.level == "ERROR"
    assert event.service == "OrderService"
    assert "Failed to create order" in event.message


def test_parse_invalid_log_line_returns_none():
    line = "this is not a valid log line"
    event = parse_line(line)

    assert event is None
