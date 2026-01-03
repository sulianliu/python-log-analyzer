from analyzer.registry import RuleRegistry
from analyzer.rules import ErrorRule
from analyzer.rules_error_count import ErrorCountRule
from analyzer.rules_service_error_count import ServiceErrorCountRule


def create_default_registry(
        error_threshold: int = 1,
        service_error_threshold: int = 1,
        service: str | None = None,
) -> RuleRegistry:
    registry = RuleRegistry()

    registry.register(ErrorRule())
    registry.register(ErrorCountRule(error_threshold))
    registry.register(
        ServiceErrorCountRule(
            threshold=service_error_threshold,
            service=service,
        )
    )

    return registry
