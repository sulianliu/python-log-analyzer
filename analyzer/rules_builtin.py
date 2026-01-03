from analyzer.registry import RuleRegistry
from analyzer.rules import ErrorRule
from analyzer.rules_error_count import ErrorCountRule


def create_default_registry(error_threshold: int = 1) -> RuleRegistry:
    registry = RuleRegistry()
    registry.register(ErrorRule())
    registry.register(ErrorCountRule(error_threshold))
    return registry
