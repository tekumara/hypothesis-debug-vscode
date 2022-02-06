MAKEFLAGS += --warn-undefined-variables
SHELL = /bin/bash -o pipefail
.DEFAULT_GOAL := help
.PHONY: help clean install format check lint pyright test hooks install-hooks

## display help message
help:
	@awk '/^##.*$$/,/^[~\/\.0-9a-zA-Z_-]+:/' $(MAKEFILE_LIST) | awk '!(NR%2){print $$0p}{p=$$0}' | awk 'BEGIN {FS = ":.*?##"}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' | sort

venv ?= .venv
pip := $(venv)/bin/pip

$(pip):
# create venv using system python even when another venv is active
	PATH=$${PATH#$${VIRTUAL_ENV}/bin:} python3 -m venv --clear $(venv)
	$(venv)/bin/python --version
	$(pip) install pip~=21.3

$(venv): setup.py $(pip)
	$(pip) install -e '.[dev]'
	touch $(venv)

# delete the venv
clean:
	rm -rf $(venv)

## create venv and install this package
install: $(venv)

## format all code
format: $(venv)
	$(venv)/bin/autoflake --in-place --recursive --remove-all-unused-imports .
	$(venv)/bin/black .
	$(venv)/bin/isort .

## lint code and run static type check
check: lint pyright

## lint using flake8
lint: $(venv)
	$(venv)/bin/flake8

## run tests
test: $(venv)
	$(venv)/bin/pytest

