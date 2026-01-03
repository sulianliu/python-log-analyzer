from argparse import ArgumentParser
from argparse import Namespace
from typing import Sequence

from analyzer.parser import parse_line
from analyzer.stats import top_services


def parse_args(argv: Sequence[str] | None = None) -> Namespace:
    parser = ArgumentParser(description="Log Analyzer CLI")
    parser.add_argument("file", help="Log file path")
    parser.add_argument("--level", default="ERROR", help="Log level to analyze")
    parser.add_argument("--top", type=int, default=3, help="Top N services")
    return parser.parse_args(argv)


def main() -> None:
    args = parse_args()
    file = args.file
    level = args.level
    top_n = args.top

    events = []

    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            event = parse_line(line)
            if event:
                events.append(event)

    results = top_services(events, level, top_n)

    print(f"Top {top_n} services with level {level}:")
    for service, count in results:
        print(f"{service}: {count}")
