from analyzer.cli import parse_args


def test_cli_with_required_file_argument():
    args = parse_args(["sample.log"])

    assert args.file == "sample.log"
    assert args.level == "ERROR"
    assert args.top == 3
