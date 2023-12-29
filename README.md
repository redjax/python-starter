# python-starter

A basic Python project starter for my own reference. It'll evolve as I learn more about packaging Python projects, hopefully 🤞

## Assumptions

This project starter makes a few assumptions:

- You're using [`pdm`](pdm-project.org/) for dependency management/builds
- You're building a library, not an application ([what's the difference](https://iscinumpy.dev/post/app-vs-library/)?)
  - I'll make another template for an application at some point
- You're developing on Linux, specifically a `Debian`-based distribution
  - May not be strictly necessary, especially with [`tox`](https://tox.wiki/en/stable/)/[`nox`](https://nox.thea.codes/en/stable/), but that's where I build most of my programs, so it's what this project is developed around
- You want to use the "`src` layout"
  - [`src` vs `flat` layouts](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/)
- You're using [`Dynaconf`](dynaconf.com/) for configuration management

## How to use

Fork or clone this repository, deleting the `.git` folder if you clone, and build up using this repository's foundation.

## Project structure

This project uses a `src` layout (as opposed to a `flat` layout). This is better for testing, as the package is built as if a user installed it, so it can be tested in isolation with `nox`/`tox`. This repository includes both `nox` and `tox`, so pick your favorite and delete the other (or delete them both if you don't use `nox`/`tox` for testing).

## Dependencies

This project has some dependencies defined already. I'll try keep this list updated, but check the [`pyproject.toml`](./pyproject.toml) file, in the `[project]` and `[tool.pdm.dev-dependencies]` sections, for the full list. The idea is to start with a minimal configuration, adding to this project only dependencies I use for *every* project.

- `pdm`:
  - The project/dependency manager
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
