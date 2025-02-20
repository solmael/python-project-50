install:
	uv sync

run:
	uv run gendiff -h

package:
	pip install -e .

lint:
	uv run ruff check