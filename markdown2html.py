#!/usr/bin/python3
"""convert Markdown file to HTML"""
import sys
import os
import re


def markdown2html(input_file, outputName):
    """convert Markdown file to HTML"""
    # Check that the Markdown file exists and is a file
    if not (os.path.exists(input_file) and os.path.isfile(input_file)):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)
