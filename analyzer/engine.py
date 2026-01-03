from typing import Iterable
from .rules import Rule
from .model import AnalysisResult, LogEntry

class AnalyzerEngine:
    def __init__(self, rules: Iterable[Rule]):
        self._rules = list(rules)

    def run(self, entries: Iterable[LogEntry]) -> list[AnalysisResult]:
        results: list[AnalysisResult] = []
        for rule in self._rules:
            results.extend(rule.analyze(entries))
        return results
