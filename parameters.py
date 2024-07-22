# параметры для запуска бота
TOKEN = '$TOKEN'
CERT = '/home/mikhailtte/certs/cert.pem'
WEBHOOK_HOST = 'https://IP:PORT'
WEBHOOK_PATH = TOKEN
WEBHOOK_URL = f"{WEBHOOK_HOST}/{WEBHOOK_PATH}"
WEBAPP_HOST = '0.0.0.0.'  # or ip
WEBAPP_PORT = 8000
LOG_FILE = 'logging.log'


# https://api.telegram.org/bot#TOKEN/setWebhook?url=https://IP:PORT/$TOKEN
# curl -F "url=https://IP:PORT/bot.py" -F "certificate=fullchain.pem" "https://api.telegram.org/botTOKEN/setwebhook"