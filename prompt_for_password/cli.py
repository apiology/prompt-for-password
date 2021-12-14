"""Console script for prompt-for-password."""
import argparse
import sys
from typing import List


def parse_argv(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    # https://docs.python.org/3/library/argparse.html
    # https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_subparsers
    subparsers = parser.add_subparsers(dest='operation')
    op1_parser = subparsers.add_parser('op1',
                                       help='Do some kind of operation',
                                       description='Do some kind of operation')
    op1_parser.add_argument('arg1', type=int, help='arg1 help')
    args = parser.parse_args(argv[1:])
    if args.operation is None:
        # Not sure why coverage doesn't recognize this, but it is in fact tested
        parser.error('Please provide a command')  # pragma: no cover
    return args


def process_args(args: argparse.Namespace) -> int:
    print("Arguments: " + str(args))
    print("Replace this message by putting your code into "
          "prompt_for_password.cli.process_args")
    return 0


def main(argv: List[str] = sys.argv) -> int:
    """Console script for prompt-for-password."""

    args = parse_argv(argv)

    return process_args(args)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover