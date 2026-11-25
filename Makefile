lint:
	uv run flake8
	uv run mypy --strict
run:
	uv run python3 -m src