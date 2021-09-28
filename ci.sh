#!/bin/bash


RED='\033[1;91m'
GREEN='\033[1;92m'
BLUE='\033[1;94m'
NC='\033[0m' # No Color

trycmd(){
    "$@"
    local status=$?
    if [ $status -ne 0 ]; then
        echo -e "${RED}Error occurred with $1 ${NC}" >&2
        exit $status
    fi
    return $status
}

trycmd python3 -m venv venv
trycmd python3 -m pip install -r requirements.dev.txt
trycmd python3 -m pip install .

export PYTHONPATH=${PWD}:${PYTHONPATH}

trycmd python3 setup.py test
trycmd coverage run tests/testsuite.py

#trycmd pylint -j4 filecompare --rcfile=${PWD}/.pylintrc || true
