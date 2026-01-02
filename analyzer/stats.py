from collections import Counter
from analyzer.model import LogEvent

def top_services(events: list[LogEvent], level: str, top_n: int) -> list[tuple[str, int]]:
    counter: Counter[str] = Counter()
    for e in events:
        if e.level == level:
            counter[e.service] += 1
    return counter.most_common(top_n)
