from collections import defaultdict
from typing import Optional

from analyzer.model import AnalysisResult


class ServiceErrorCountRule:
    name = "service-error-count"

    def __init__(self, threshold: int, service: Optional[str] = None):
        if threshold <= 0:
            raise ValueError("threshold must be positive")
        self._threshold = threshold
        self._service = service  # None = all services

    def analyze(self, entries):
        counts: dict[str | None, int] = defaultdict(int)

        for e in entries:
            if e.level != "ERROR":
                continue

            if self._service is not None and e.service != self._service:
                continue

            counts[e.service] += 1

        results: list[AnalysisResult] = []

        for service, count in counts.items():
            if count >= self._threshold:
                svc = service or "<unknown>"
                results.append(
                    AnalysisResult(
                        rule=self.name,
                        detail=(
                            f"service={svc}, "
                            f"errors={count}, "
                            f"threshold={self._threshold}"
                        ),
                        line=None,
                    )
                )

        return results
