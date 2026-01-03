from typing import Dict, Iterable
from analyzer.rules import Rule

class RuleRegistry:
    def __init__(self):
        self._rules: Dict[str, Rule] = {}

    def register(self, rule: Rule) -> None:
        if rule.name in self._rules:
            raise ValueError(f"Duplicate rule name: {rule.name}")
        self._rules[rule.name] = rule

    def get(self, name: str) -> Rule:
        return self._rules[name]

    def all(self) -> Iterable[Rule]:
        return self._rules.values()

    def select(self, names: Iterable[str]) -> list[Rule]:
        return [self._rules[name] for name in names]
