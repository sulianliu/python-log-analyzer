import argparse

from analyzer.engine import AnalyzerEngine
from analyzer.parser import parse_lines
from analyzer.rules_builtin import create_default_registry


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    parser.add_argument(
        "--rules",
        help="Comma-separated rule names (default: all)",
    )
    parser.add_argument(
        "--error-threshold",
        type=int,
        default=1,
        help="Minimum number of ERROR logs to trigger error-count rule",
    )
    args = parser.parse_args()

    with open(args.file) as f:
        entries = parse_lines(f)

    registry = create_default_registry(
        error_threshold=args.error_threshold
    )

    if args.rules:
        rule_names = [r.strip() for r in args.rules.split(",")]
        rules = registry.select(rule_names)
    else:
        rules = list(registry.all())

    engine = AnalyzerEngine(rules)
    results = engine.run(entries)

    for r in results:
        print(r)


if __name__ == "__main__":
    main()
