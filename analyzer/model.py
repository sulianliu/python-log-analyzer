from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class LogEvent:
    timestamp: datetime
    level: str
    service: str
    message: str
