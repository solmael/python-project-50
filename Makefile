install:
	uv sync

run:
	uv run gendiff -h

package:
	pip install -e .