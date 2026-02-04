import os
import urllib.parse
import urllib.request

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram_message(token, chat_id, text):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = urllib.parse.urlencode({
        "chat_id": chat_id,
        "text": text
    }).encode("utf-8")

    req = urllib.request.Request(url, data=data, method="POST")
    with urllib.request.urlopen(req, timeout=20) as resp:
        resp.read()

def main():
    # DEBUG TOTAL
    if not TELEGRAM_BOT_TOKEN:
        raise RuntimeError("❌ TELEGRAM_BOT_TOKEN não existe no ambiente")

    if not TELEGRAM_CHAT_ID:
        raise RuntimeError("❌ TELEGRAM_CHAT_ID não existe no ambiente")

    send_telegram_message(
        TELEGRAM_BOT_TOKEN,
        TELEGRAM_CHAT_ID,
        "🚀 TESTE OK — Python rodou e o Telegram respondeu"
    )

if __name__ == "__main__":
    main()
