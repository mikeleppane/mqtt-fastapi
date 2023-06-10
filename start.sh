#!/bin/bash

set -euo pipefail

poetry run aerich upgrade && poetry run gunicorn --bind 0.0.0.0:8800 src.main:app -k uvicorn.workers.UvicornWorker
