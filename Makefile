SRC_DIR = ./src/

.PHONY: check fix schema run

check:
	poetry run mypy --version
	poetry run mypy $(SRC_DIR)
	poetry run black --version
	poetry run black --check --line-length=100 $(SRC_DIR)
	poetry run isort --version
	poetry run isort --check-only $(SRC_DIR)
	poetry run ruff --version
	poetry run ruff check $(SRC_DIR)

fix:
	poetry run black --line-length=100 $(SRC_DIR)
	poetry run isort $(SRC_DIR)
	poetry run ruff check --fix $(SRC_DIR)


run:
	poetry run aerich upgrade && poetry run uvicorn src.main:app --reload --reload-exclude tests --port $${BACKEND_PORT:-8800} --host 0.0.0.0

test:
	poetry run pytest -v tests/

test-unit:
	poetry run pytest -v tests/unit

test-integration:
	poetry run pytest -v tests/integration

cov:
	poetry run pytest -v --cov="."