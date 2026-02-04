import urllib.request
import urllib.parse
import os

token = os.environ["TELEGRAM_BOT_TOKEN"]
chat_id = os.environ["TELEGRAM_CHAT_ID"]

url = f"https://api.telegram.org/bot{token}/sendMessage"
data = urllib.parse.urlencode({
    "chat_id": chat_id,
    "text": "🚨 TESTE FINAL ABSOLUTO: se isso chegou, tá 100% funcionando."
}).encode("utf-8")

req = urllib.request.Request(url, data=data, method="POST")
urllib.request.urlopen(req, timeout=20)

print("Mensagem enviada para o Telegram")
