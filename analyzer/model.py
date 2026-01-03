from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass(frozen=True)
class LogEntry:
    timestamp: datetime
    level: str
    message: str
    service: Optional[str] = None


@dataclass(frozen=True)
class AnalysisResult:
    rule: str
    detail: str
    line: Optional[int]
