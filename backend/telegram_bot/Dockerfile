# backend/telegram_bot/Dockerfile
FROM python:3.12

# Устанавливаем необходимые системные зависимости
RUN apt-get update && apt-get install -y \
    curl \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && ln -s /root/.local/bin/poetry /usr/local/bin/poetry

# Устанавливаем рабочую директорию
WORKDIR /app
# Копируем файлы проекта
COPY pyproject.toml poetry.lock ./

# Устанавливаем зависимости с помощью poetry
RUN poetry install --no-root --no-dev

# Копируем остальной код
COPY . .
RUN chmod +x entrypoint.sh
# Открываем порт (если ваш сервис использует какой-либо порт)
# EXPOSE 8000  # Укажите, если ваш сервис работает на определенном порту

# Команда запуска сервиса
CMD ["poetry", "run", "python", "main.py"]
