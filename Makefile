UV := env UV_PROJECT_ENVIRONMENT=/tmp/ai-bio-discovery-venv UV_CACHE_DIR=/tmp/uv-cache UV_LINK_MODE=copy uv
ADAMSON_ARCHIVE := data/raw/adamson_gears/archive/adamson.zip
ADAMSON_WORK_DIR := /tmp/ai-bio-discovery/adamson-working
ADAMSON_H5AD := $(ADAMSON_WORK_DIR)/adamson/perturb_processed.h5ad

.PHONY: setup verify test lint check verify-adamson prepare-adamson inspect-adamson walkthrough-adamson quality-adamson

setup:
	$(UV) sync --frozen --group dev

verify:
	$(UV) run python scripts/check_environment.py

test:
	$(UV) run pytest -q

lint:
	$(UV) run ruff check .

check: setup verify test lint

verify-adamson:
	echo "0bde631bae60ee8c105991ff0e0d4a20  $(ADAMSON_ARCHIVE)" | md5sum --check -

prepare-adamson: verify-adamson
	mkdir -p $(ADAMSON_WORK_DIR)
	unzip -oq $(ADAMSON_ARCHIVE) -d $(ADAMSON_WORK_DIR)
	test "$$(stat -c %s $(ADAMSON_H5AD))" = "606502516"

inspect-adamson: setup prepare-adamson
	$(UV) run python scripts/inspect_h5ad.py $(ADAMSON_H5AD) --output data/processed/adamson_metadata.json

walkthrough-adamson: setup prepare-adamson
	$(UV) run python scripts/create_adamson_walkthrough.py $(ADAMSON_H5AD) --output-dir artifacts/data_walkthrough

quality-adamson: setup prepare-adamson
	$(UV) run python scripts/check_adamson_quality.py $(ADAMSON_H5AD) --output artifacts/data_quality/adamson_quality.json
