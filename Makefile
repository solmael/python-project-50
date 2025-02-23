install:
	uv sync

run:
	uv run gendiff -h

package:
	pip install -e .

lint:
	uv run ruff check

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml