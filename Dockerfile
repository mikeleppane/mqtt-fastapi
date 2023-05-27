# pull official base image
FROM python:3.11.3-slim-buster

# set working directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN adduser --group --system appuser

# install system dependencies
RUN set -eux; \
    apt-get update; \
    apt-get install --no-install-recommends netcat curl gcc make -y; \
    apt-get clean; \
    pip install --upgrade pip; \
    pip3 install poetry

COPY poetry.lock .
COPY pyproject.toml .

RUN poetry config virtualenvs.create false
RUN poetry install --no-root

COPY . .

RUN chmod 755 /app/entrypoint.sh

USER appuser

# run entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]