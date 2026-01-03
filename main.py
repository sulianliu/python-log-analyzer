from analyzer.cli import parse_args
from analyzer.parser import parse_line
from analyzer.stats import top_services


def main() -> None:
    args = parse_args()
    events = []

    with open(args.file, "r", encoding="utf-8") as f:
        for line in f:
            event = parse_line(line)
            if event:
                events.append(event)

    results = top_services(events, args.level, args.top)

    print(f"Top {args.top} services with level {args.level}:")
    for service, count in results:
        print(f"{service}: {count}")


if __name__ == "__main__":
    main()
