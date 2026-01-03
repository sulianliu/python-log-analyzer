from typing import Protocol, Iterable

from .model import LogEntry, AnalysisResult


class Rule(Protocol):
    def analyze(self, events: Iterable[LogEntry]) -> list[AnalysisResult]:
        ...


class ErrorRule:
    name = "error-detection"

    def analyze(self, entries):
        results = []
        for i, e in enumerate(entries):
            if e.level == "ERROR":
                results.append(
                    AnalysisResult(
                        rule=self.name,
                        detail=e.message,
                        line=i + 1,
                    )
                )
        return results
