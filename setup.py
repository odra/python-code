#!/usr/bin/env python                                                                                                                               
from setuptools import setup, find_packages


setup(
  name='python code object sumatra module for python sdk and runner.',
  version='0.0.1',
  description='Manages and builds code and function objects.',
  author='Sumatra',
  packages=find_packages(),
  install_requires=[
    'six==1.10.0',
    'schematics==1.1.1'
  ],
  tests_require=['pytest', 'pytest-sugar']
)
