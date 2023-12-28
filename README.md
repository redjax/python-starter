# python-starter

A basic Python project starter for my own reference. It'll evolve as I learn more about packaging Python projects, hopefully 🤞

## Project structure

This project uses a `src` layout (as opposed to a `flat` layout). This is better for testing, as the package is built as if a user installed it, so it can be tested in isolation with `nox`/`tox`.

## Dev Dependencies

I've pre-installed a number of development dependencies, which I manage with `pdm`. I'll try keep this list updated, but check the [`pyproject.toml`](./pyproject.toml) file, under `[tool.pdm.dev-dependencies]`, for the full list.

- `pdm`:
  - The dependency manager that installs these development dependencies
- `black`
  - For formatting code
- `ruff`
  - For linting/checking code
- `pytest`
  - The test suite
- `pytest-xdg`
  - Library for allowing concurrent test execution
- Test standardization tools (I want both examples to be available, but in a real project I would choose only 1)
- `nox`
  - Test standardization tool that uses regular Python files
  - More flexible, but more error prone (in my experience)
    - Example: When I have multiple Python environment versions in my `pyenv global` path, `tox` recognizes and uses each one without issue. Trying to do the same with `nox` doesn't work, I have to manually switch my `pyenv shell` to the environment I want to test. I'm open to the possibility I'm doing it wrong, but it "just works" with `tox`
- `tox`
  - Test standardization tool that uses a `tox.ini` file, with a yaml-esque DSL
  - I am leaning more towards `tox` because it's easier to find help & examples online, and also becaause I've had more luck with it, generally.
