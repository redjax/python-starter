FROM python:3.11-slim AS base

## Set ENV variables to control Python/pip behavior inside container
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    ## Pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    PDM_IGNORE_ACTIVE_ENV=1

FROM base AS build

WORKDIR /app

COPY requirements/requirements.ci.txt requirements.txt
RUN python -m pip install -r requirements.txt
RUN python -m pip install pdm

FROM build AS stage

WORKDIR /app

COPY pyproject.toml /app/pyproject.toml
COPY pdm.lock /app/pdm.lock
COPY src/ /app/src
COPY tests/ /app/tests
COPY noxfile.py /app/noxfile.py
COPY tox.ini /app/tox.ini
COPY ruff.ci.toml /app/ruff.ci.toml

FROM stage AS run

WORKDIR /app

COPY --from=stage /app .

RUN ls -la . && sleep 10

RUN ["python", "-m", "pdm", "run", "nox"]
