#!/bin/bash

set -euo pipefail

aerich upgrade && gunicorn --bind 0.0.0.0:8800 src.main:app -k uvicorn.workers.UvicornWorker
