.PHONY: run install unit integration test lint format

run: install
	@poetry run python3 src/main.py

install:
	poetry install

unit: install
	@poetry run pytest test/unit

integration: install
	@poetry run pytest test/integration

test: unit integration

lint:
	poetry run mypy src
	poetry run ruff check src
	poetry run ruff format --check src

format:
	poetry run ruff format src
	poetry run ruff check --fix src