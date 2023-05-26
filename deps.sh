#!/usr/bin/env bash

set -eu

docker run --rm -v $(pwd):/w -w /w --entrypoint python public.ecr.aws/lambda/python:3.10 -m pip install --target ./package -r requirements.txt
rm -f ./package.zip
pushd package
zip -rq ../package.zip .
popd

