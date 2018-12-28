"""Command line interface.
"""
import argparse
import logging
from pathlib import Path
import sys

from mutatest.controller import run_trials

LOGGER = logging.getLogger(__name__)
FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"


def run_all():
    parser = argparse.ArgumentParser(description="Run mutation tests.")

    parser.add_argument(
        "-p",
        "--pkg",
        required=True,
        type=str,
        help="Target package directory for mutation testing.",
    )
    parser.add_argument(
        "-t",
        "--testcmds",
        required=False,
        default="pytest",
        type=str,
        help="Test command string to execute, default to 'pytest' if empty.",
    )
    parser.add_argument(
        "-d", "--debug", action="store_true", help="Turn on DEBUG level logging output."
    )

    args = parser.parse_args()

    pkg_dir = Path(args.pkg)
    test_cmds = args.testcmds.split()

    logging.basicConfig(
        format=FORMAT,
        level=logging.DEBUG if args.debug else logging.INFO,
        stream=sys.stdout,
    )


    run_trials(pkg_dir=pkg_dir, test_cmds=test_cmds)

