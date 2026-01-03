from analyzer.registry import RuleRegistry


class DummyRule:
    name = "dummy"

    def analyze(self, entries):
        return []


def test_registry_register_and_get():
    registry = RuleRegistry()
    rule = DummyRule()

    registry.register(rule)

    assert registry.get("dummy") is rule
