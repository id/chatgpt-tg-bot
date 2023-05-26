#!/usr/bin/env bash

set -eu

aws --profile chatgpt-tg-bot --region eu-north-1 lambda update-function-code --function-name chatgpt-tg-bot --zip-file fileb://package.zip
