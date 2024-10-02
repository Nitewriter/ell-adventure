# Makefile for the ell-adventure project

# Path to the virtual environment
VENV := .venv
POETRY := poetry
PYTHON := $(POETRY) run python

# Activate virtual environment
$(VENV): pyproject.toml poetry.lock
	$(POETRY) install
	touch $(VENV)

# Linting target
.PHONY: lint
lint: $(VENV)
	@echo "Running ruff for linting..."
	$(POETRY) run ruff check .

# Test target
.PHONY: test
test: $(VENV)
	@echo "Running pytest..."
	$(POETRY) run pytest

# Formatting target
.PHONY: format
format:
	@echo "Running ruff for fixing lint issues..."
	ruff check --fix .
	@echo "Sorting pyproject.toml with toml-sort..."
	toml-sort pyproject.toml

# Check target to run both linting and formatting checks
.PHONY: check
check: lint format
	@echo "Linting and formatting checks completed."

# Default target
.PHONY: all
all: lint test
	@echo "All checks completed."

# Clean target
.PHONY: clean
clean:
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete

# Update dependencies
.PHONY: update-deps
update-deps:
	$(POETRY) update