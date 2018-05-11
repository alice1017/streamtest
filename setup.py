#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages
from streamtest import (
    __author__,
    __author_email__,
    __version__,
    __license__
)

setup(
    name="streamtest",
    author=__author__,
    author_email=__author_email__,
    description="Python unittest.TestCase for testing the output of "
                "standard stream(stdout, stderr)",
    version=__version__,
    license=__license__,
    packages=find_packages()
)
