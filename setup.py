#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Setuptools-based setup module."""

from setuptools import setup, find_packages

INSTALL_REQUIRES = ['numpy',
                    'scipy']

EXTRAS_REQUIRE = {'analysis': ['matplotlib']}

setup(
    name='thrifty',
    version='0.0.1',
    description='Proof-of-concept SDR software for TDOA positioning',
    author='Schalk-Willem Krüger',
    python_requires=">=3.10",
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    packages=find_packages(exclude=('tests', 'docs', 'old')),
    entry_points={
        'console_scripts': [
            'thrifty = thrifty.cli:_main'
        ]
    },
)
