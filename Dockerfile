FROM python:3.11-slim-buster

WORKDIR /app

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  # pip:
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  # poetry:
  POETRY_VERSION=0.1.0 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_CACHE_DIR='/var/cache/pypoetry'

RUN pip install poetry && poetry --version

COPY ./poetry.lock ./pyproject.toml ./README.md /app/

RUN poetry install --no-root

COPY  . .

CMD ["python", "/app/main.py"]