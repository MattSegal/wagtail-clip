#!/bin/bash
# Publishes the package to PyPI.
# Requires twine
set -e
rm -rf build/ dist/ wagtailclip.egg-info/
python3 setup.py bdist_wheel sdist
twine upload dist/*
rm -rf build/ dist/ wagtailclip.egg-info/
