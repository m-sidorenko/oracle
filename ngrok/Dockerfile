FROM ngrok/ngrok:latest

# Переключаемся на суперпользователя для установки пакетов и изменения прав
USER root

# Устанавливаем curl и jq
RUN apt-get update && apt-get install -y curl jq

# Копируем и изменяем права на скрипт
COPY start_ngrok.sh /app/start_ngrok.sh
RUN chmod +x /app/start_ngrok.sh

# Переключаемся обратно в обычного пользователя
USER ngrok

WORKDIR /app

ENTRYPOINT ["/bin/bash", "/app/start_ngrok.sh"]