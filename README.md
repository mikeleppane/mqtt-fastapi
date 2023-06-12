[![FastAPI/MQTT - Continuous Integration](https://github.com/mikeleppane/mqtt-fastapi/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/mikeleppane/mqtt-fastapi/actions/workflows/ci.yml)

# FastAPI and MQTT

## What it is

A Python application that subscribes to an MQTT topic, logs the received messages and persists them. The application
also exposes an api endpoint to get all the messages.

## How to use it

The project runs inside a docker container.
Make sure you have Docker and Docker Compose installed. After that simply run
the following command in the project root:

```
docker compose up -d
```

This will expose the backend (fastapi) a host/port at

```bash
http://0.0.0.0:8800
```

In addition, MQTT broker is exposed at host/port

```bash
http://0.0.0.0:1883
```

By default, the subscription service listens to a topic ***humidity/outside*** but user can
change this with TOPIC environment variable (see docker-compose.yml file).

You can use e.g. [MQTT X](https://mqttx.app/) to publish a message to a topic on a broker.

## REST API

### Health check

#### GET /v1/health_check

Checks that the app is ok.

Response payload:

```
{
  "message": "OK"
}
```

### Messges

#### GET /v1/messages

Get all stored messages ordered by timestamp

Example response payload:

```
[
  {
    "created_at": "2023-06-05T10:01:08.587763",
    "payload": "{\"humidity\": 5.66}"
  },
  {
    "created_at": "2023-06-05T09:59:21.040788",
    "payload": "{\"humidity\": 0.75}"
  }
]
```

## Development

The project contains a separate docker compose file a local development.

```
docker compose -f docker-compose.dev.yml up -d
```

The Makefile contains a few targets to help the development for instance:

Run the tests:

```
docker compose exec backend make test
```

Run the checks

```
docker compose exec backend make check
```

## Used Tech

- [Python (3.11)](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [MQTT](https://mqtt.org/)
- [Docker](https://www.docker.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [Tortoise ORM](https://tortoise.github.io/)


