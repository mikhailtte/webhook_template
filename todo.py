# открыть порт 443
# установить nginx
# сгенерировать самоподписные серификаты командой с сайта телеграма: 
# openssl req -newkey rsa:2048 -sha256 -nodes -keyout private.key -x509 -days 365 -out cert.pem
# путь на внутреннем и внешнем интерфейсе нужно проименовать токеном бота

TOKEN = 'TOKEN_HERE'
CERT = '/home/mikhailtte/certs/cert.pem'
WEBHOOK_HOST = 'https://IP:PORT'
WEBHOOK_PATH = TOKEN
WEBHOOK_URL = f"{WEBHOOK_HOST}/{WEBHOOK_PATH}"
WEBAPP_HOST = '0.0.0.0.'  # or ip
WEBAPP_PORT = 8000
LOG_FILE = 'logging.log'

# по пути /etc/nginx/sites-available/myapp прописать настройки соединения, внешний и внутренние пути сервера
# прописать путь до серитфикатов
# server {
#   listen 80;
#   listen 443 ssl;
#   server_name https://185.116.193.204;
#   ssl_certificate /home/tte/certs/cert.pem;
#   ssl_certificate_key /home/tte/certs/private.key;

#   location /$TOKEN {
#     proxy_pass http://0.0.0.0:8000/$TOKEN;
#     proxy_http_version 1.1;
#     proxy_set_header Upgrade $http_upgrade;
#     proxy_set_header Host $host;
#     proxy_redirect off;
#     proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
#     proxy_set_header X-Real-IP $remote_addr;
#     proxy_set_header X-Scheme $scheme;
#     proxy_set_header X-Forwarded-Host $host;
#   }
# }
# запустить nginx: systemctl start/restart nginx
# телеграм бот запустить обычной командой из любого места сервера
# телегрмау необходимо указать адрес для вебхуков и активировать их запросом: 
# https://api.telegram.org:443/bot$TOKEN/setWebhook?url=https://IP:PORT/$TOKEN
# проверить состояние подключения запросом: https://api.telegram.org/bot$TOKEN/getWebhookInfo

# таким образом nginx будет слушать внешний адрес и порт по данной ссылке и перенаправлять пакеты на внутренний, на внутреннм будет сидеть
# программа и отвечать на данные запрсы в обратном направлении