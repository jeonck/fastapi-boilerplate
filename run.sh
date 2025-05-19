#!/bin/bash

# 명시적으로 올바른 VIRTUAL_ENV 환경 변수 설정
export VIRTUAL_ENV=$(pwd)/.venv

# uv run 명령 실행
uv run run.py "$@"