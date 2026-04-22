#!/bin/sh -eu
cd "$(dirname "${0}")"
hatch build -c -t wheel
