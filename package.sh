#!/usr/bin/env bash

set -eu

[ ! -f package.zip ] && ./deps.sh
zip -g package.zip lambda_function.py
