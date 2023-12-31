# Используйте официальный образ Python
FROM python:3.12-slim-buster

# Установите рабочую директорию в /app
WORKDIR /app

# Установите переменные окружения для poetry
ENV POETRY_VERSION=1.7.1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/app" \
    VENV_PATH="/app/.venv"
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# Установите poetry
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    apt-get purge -y --auto-remove curl

# Копируйте только файлы зависимостей, чтобы воспользоваться кэшированием Docker
COPY pyproject.toml poetry.lock ./

# Установите зависимости
RUN poetry install --no-dev

# Копируйте остальные файлы проекта
COPY . .

# Запустите бота
CMD ["python", "main.py"]
