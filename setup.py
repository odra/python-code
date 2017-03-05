#!/usr/bin/env python                                                                                                                               
from setuptools import setup, find_packages


setup(
  name='python code object sumatra module',
  version='0.0.1',
  description='Manages and builds code object type.',
  author='Sumatra',
  packages=find_packages(),
  install_requires=[
    'six==1.10.0',
    'Sphinx==1.5.1',
    'pytest==3.0.5'
  ],
  setup_requires=['pytest-runner'],
  tests_require=['pytest', 'pytest-sugar']
)
