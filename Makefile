UV := env UV_PROJECT_ENVIRONMENT=/tmp/ai-bio-discovery-venv UV_CACHE_DIR=/tmp/uv-cache UV_LINK_MODE=copy uv

.PHONY: setup verify test lint check

setup:
	$(UV) sync --frozen --group dev

verify:
	$(UV) run python scripts/check_environment.py

test:
	$(UV) run pytest -q

lint:
	$(UV) run ruff check .

check: setup verify test lint

