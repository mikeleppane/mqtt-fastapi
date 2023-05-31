# pull official base image
FROM python:3.11.3-slim-buster

# set working directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PATH="${PATH}:/root/.local/bin"

# install system dependencies
RUN set -eux; \
    apt-get update; \
    apt-get install --no-install-recommends netcat curl gcc make -y; \
    apt-get clean; \
    pip install --upgrade pip; \
    curl -sSL https://install.python-poetry.org | python3 -

COPY poetry.lock .
COPY pyproject.toml .

RUN poetry install --no-root

COPY . .

RUN chmod 755 /app/entrypoint.sh

# run entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]