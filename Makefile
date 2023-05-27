MAIN_FILE = ./src/main.py
SRC_DIR = ./src/mqtt_fastapi

.PHONY: check fix schema run

check:
	poetry run mypy --version
	poetry run mypy $(MAIN_FILE) $(SRC_DIR)
	poetry run black --version
	poetry run black --check --line-length=100 $(MAIN_FILE) $(SRC_DIR)
	poetry run isort --version
	poetry run isort --check-only $(MAIN_FILE) $(SRC_DIR)
	poetry run ruff --version
	poetry run ruff check $(MAIN_FILE) $(SRC_DIR)

fix:
	poetry run black --line-length=100 $(SRC_DIR)
	poetry run isort $(MAIN_FILE) $(SRC_DIR)
	poetry run ruff check --fix $(MAIN_FILE) $(SRC_DIR)


run:
	poetry run uvicorn src.main:app --reload --reload-exclude test*.* --port 8800 --host 0.0.0.0