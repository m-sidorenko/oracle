export $(cat /shared_env/.env.backend | xargs) 
poetry run python main.py