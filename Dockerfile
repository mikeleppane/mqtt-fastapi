# pull official base image
FROM python:3.11.3-slim-bullseye

# set working directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PATH="${PATH}:/root/.local/bin"

# install system dependencies
RUN set -eux; \
    export DEBIAN_FRONTEND=noninteractive; \
    apt-get update; \
    apt-get -y upgrade; \
    apt-get install --no-install-recommends curl make gcc -y; \
    apt-get clean; \
    rm -rf /var/lib/apt/lists/*; \
    pip install --upgrade pip; \
    curl -sSL https://install.python-poetry.org | python3 -

COPY poetry.lock .
COPY pyproject.toml .

RUN poetry install --no-root

COPY . .

CMD ["make", "run"]