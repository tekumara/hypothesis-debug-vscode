# hdebug

Hypothesis debugging with vscode.
Reproduction of debugpy issue [#847](https://github.com/microsoft/debugpy/issues/837).

## Getting started

Prerequisites:

- make
- python >= 3.7

To start:

- Install the [development environment](CONTRIBUTING.md#Development-environment): `make install`

To demonstrate the issue:

- set a breakpoint on line 10 in [tests/test_example.py](tests/test_example.py)
- in the terminal activate the virtualenv if needed: `. .venv/bin/activate`
- run `hdebug`
- in vscode run the `Attach to 62888` launch config
- observe that the breakpoint is not hit
