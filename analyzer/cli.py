import argparse
from typing import Sequence


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Log Analyzer CLI")
    parser.add_argument("file", help="Log file path")
    parser.add_argument("--level", default="ERROR", help="Log level to analyze")
    parser.add_argument("--top", type=int, default=3, help="Top N services")
    return parser.parse_args(argv)
