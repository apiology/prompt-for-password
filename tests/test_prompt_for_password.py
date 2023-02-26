#!/usr/bin/env python

"""Tests for `prompt_for_password` package."""

# from prompt_for_password import prompt_for_password
import os
import subprocess
import sys

import pytest


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_dunders(response):
    assert prompt_for_password.__author__ is not None
    assert prompt_for_password.__email__ is not None
    assert prompt_for_password.__version__ is not None


def test_cli_no_command():
    request_long_lines = {'COLUMNS': '999', 'LINES': '25'}
    env = {}
    env.update(os.environ)
    env.update(request_long_lines)
    expected_help = """usage: prompt-for-password [-h] [--prompt PROMPT] description
prompt-for-password: error: the following arguments are required: description
"""
    result = subprocess.run(['prompt-for-password'],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            env=env)
    actual_help = result.stderr.decode('utf-8')
    assert actual_help == expected_help


def test_cli_help():
    request_long_lines = {'COLUMNS': '999', 'LINES': '25'}
    env = {}
    env.update(os.environ)
    env.update(request_long_lines)
    expected_help = """usage: prompt-for-password [-h] [--prompt PROMPT] description

Request password from user and echo back on stdout

positional arguments:
  description      String to present to user when asking for secret

options:
  -h, --help       show this help message and exit
  --prompt PROMPT  Type of input being asked for
"""
    if sys.version_info <= (3, 10):
        # 3.10 changed the wording a bit
        expected_help = expected_help.replace('options:', 'optional arguments:')

    actual_help = subprocess.check_output(['prompt-for-password', '--help'],
                                          env=env).decode('utf-8')
    assert actual_help == expected_help
