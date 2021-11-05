"""Command line interface to case changer"""

import sys

from .casechange import lowercase_stream, uppercase_stream


def to_lower():
    lowercase_stream(sys.stdin, sys.stdout)


def to_upper():
    uppercase_stream(sys.stdin, sys.stdout)
