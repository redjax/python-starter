FROM python:3.11-slim AS base

## Set ENV variables to control Python/pip behavior inside container
ENV PYTHONDONTWRITEBYTECODE 1 \
    PYTHONUNBUFFERED 1 \
    ## Pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

FROM base AS build

WORKDIR /app

COPY requirements/requirements.ci.txt requirements.txt
RUN python -m pip install -r requirements.txt

FROM build AS dev

WORKDIR /app

COPY src/ tests/ noxfile.py tox.ini ruff.ci.toml ./

FROM build AS run

WORKDIR /app

RUN python -m nox
