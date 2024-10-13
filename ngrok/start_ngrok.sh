#!/bin/bash

# Аутентификация в Ngrok
ngrok config add-authtoken $NGROK_AUTHTOKEN

# Запуск Ngrok и ожидание его готовности
ngrok http 3000 &  # Запускаем Ngrok в фоновом режиме

# Ожидаем, пока Ngrok поднимется
sleep 5

# Получаем публичный URL через API Ngrok
NGROK_URL=$(curl -s http://localhost:4040/api/tunnels | jq -r '.tunnels[0].public_url')

# Записываем результат в файл .env.backend, который будет читаться в docker-compose.yaml
echo "NGROK_URL=$NGROK_URL" > /shared_env/.env.backend

# Не завершаем процесс, оставляем ngrok работающим
wait