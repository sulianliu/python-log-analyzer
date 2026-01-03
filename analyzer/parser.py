from datetime import datetime
from typing import Iterable

from analyzer.model import LogEntry


def parse_lines(lines: Iterable[str]) -> list[LogEntry]:
    entries: list[LogEntry] = []

    for line in lines:
        parts = line.strip().split(" ", 3)

        if len(parts) < 3:
            continue

        ts_raw = parts[0]

        try:
            timestamp = datetime.fromisoformat(ts_raw)
        except ValueError:
            # 非法 timestamp，直接跳过（或未来加 warning rule）
            continue

        if len(parts) == 3:
            # 旧格式：timestamp level message
            level, message = parts[1], parts[2]
            service = None
        else:
            # 新格式：timestamp service level message
            service, level, message = parts[1], parts[2], parts[3]

        entries.append(
            LogEntry(
                timestamp=timestamp,
                level=level,
                message=message,
                service=service,
            )
        )

    return entries
