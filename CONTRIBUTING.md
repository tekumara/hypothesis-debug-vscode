# Contributing 🌳

## Development environment

`make install` creates the dev environment with:

- a virtualenv in _.venv/_
- pyright in _node_modules/_
- git hooks for formatting & linting on git push

`. .venv/bin/activate` activates the virtualenv.

Run `make` to see the options for running checks, tests etc. make targets that use the virtualenv will update it when _setup.py_ changes.
