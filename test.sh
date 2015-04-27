#!/usr/bin/env bash
# Exit upon first failure
set -e

# Allow for skipping lint during development
if test "$SKIP_LINT" != "TRUE"; then
  flake8 *.py api_pagination/
fi

# Run our tests
ENV=test nosetests $* api_pagination/test/*.py
