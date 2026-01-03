from typing import Iterable

from .model import AnalysisResult, LogEntry
from .rules import Rule


class AnalyzerEngine:
    def __init__(self, rules: Iterable[Rule]):
        self._rules = list(rules)

    def run(self, entries: Iterable[LogEntry]) -> list[AnalysisResult]:
        results: list[AnalysisResult] = []
        for rule in self._rules:
            results.extend(rule.analyze(entries))
        return results
