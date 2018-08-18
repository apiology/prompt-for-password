#!/usr/bin/env python3

import pysectools
import argparse
from pysectools.pinentry import Pinentry


def main() -> None:
    desc = 'Request password from user and echo back on stdout'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('description', type=str,
                        help='String to present to user when '
                        'asking for secret')
    parser.add_argument('--prompt', type=str,
                        help='Type of input being asked for',
                        default='Password:')

    args = parser.parse_args()

    # Prevent secrets from leaking out of your process's memory:
    pysectools.disallow_swap()
    pysectools.disallow_core_dumps()

    pinentry = Pinentry(fallback_to_getpass=False)

    # all parameters are optional
    prompt: str = args.prompt
    description: str = args.description
    password: str = pinentry.ask(prompt=prompt, description=description)
    pinentry.close()
    print(password)
    pysectools.zero(password)


if __name__ == "__main__":
    main()
