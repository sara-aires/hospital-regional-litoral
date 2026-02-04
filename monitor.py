import os
import urllib.parse
import urllib.request

print(">>> ARQUIVO monitor.py CARREGADO <<<")

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram_message(token, chat_id, text):
    print(">>> ENVIANDO MENSAGEM PRO TELEGRAM <<<")

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = urllib.parse.urlencode({
        "chat_id": chat_id,
        "text": text
    }).encode("utf-8")

    req = urllib.request.Request(url, data=data, method="POST")

    with urllib.request.urlopen(req, timeout=20) as resp:
        body = resp.read().decode("utf-8", errors="replace")
        print(">>> RESPOSTA DO TELEGRAM <<<")
        print(body)
        
def main():
    print(">>> MAIN INICIOU <<<")

    if not TELEGRAM_BOT_TOKEN:
        raise RuntimeError("TOKEN NÃO EXISTE")

    if not TELEGRAM_CHAT_ID:
        raise RuntimeError("CHAT ID NÃO EXISTE")

    send_telegram_message(
        TELEGRAM_BOT_TOKEN,
        TELEGRAM_CHAT_ID,
        "🚀 TESTE DEFINITIVO — se você recebeu isso, tá TUDO funcionando"
    )

    print(">>> SCRIPT TERMINOU <<<")

if __name__ == "__main__":
    main()
