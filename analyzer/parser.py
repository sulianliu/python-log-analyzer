from datetime import datetime
from analyzer.model import LogEvent

def parse_line(line: str) -> LogEvent | None:
    parts = line.strip().split(" ", 4)
    if len(parts) < 5:
        return None

    try:
        timestamp = datetime.strptime(
            f"{parts[0]} {parts[1]}",
            "%Y-%m-%d %H:%M:%S"
        )
        level = parts[2]
        service = parts[3]
        message = parts[4]
        return LogEvent(timestamp, level, service, message)
    except ValueError:
        return None
