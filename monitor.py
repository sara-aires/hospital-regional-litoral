import urllib.request
import urllib.parse
import os

URL = "https://isgsaude.org.br/hrln/trabalhe-conosco/"
KEYWORD = "HRLN – RESULTADO FINAL E CONVOCAÇÃO – TÉCNICO DE TI 4º LUGAR 004-2025"
FLAG_FILE = "notified_test.txt"

TELEGRAM_BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
TELEGRAM_CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

def send_telegram(text: str):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = urllib.parse.urlencode({
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text
    }).encode("utf-8")

    req = urllib.request.Request(url, data=data, method="POST")
    urllib.request.urlopen(req, timeout=20)

def main():
    req = urllib.request.Request(
        URL,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    html = urllib.request.urlopen(req, timeout=20).read().decode(
        "utf-8", errors="ignore"
    )

    if KEYWORD in html:
        send_telegram(
            "✅ TESTE OK!\n\n"
            "O monitor encontrou a convocação do\n"
            "TÉCNICO DE TI – 4º LUGAR.\n\n"
            "O bot está funcionando certinho 👍"
        )
        print("Mensagem de teste enviada.")
    else:
        print("Texto do 4º lugar não encontrado.")

if __name__ == "__main__":
    main()
