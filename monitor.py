import urllib.request
import urllib.parse
import os

URL = "https://isgsaude.org.br/hrln/trabalhe-conosco/"
KEYWORD = "HRLN – RESULTADO FINAL E CONVOCAÇÃO – TÉCNICO DE TI 6º LUGAR 004-2025"
FLAG_FILE = "notified.txt"

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

def already_notified():
    return os.path.exists(FLAG_FILE)

def mark_notified():
    with open(FLAG_FILE, "w", encoding="utf-8") as f:
        f.write("ok")

def main():
    req = urllib.request.Request(
        URL,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    html = urllib.request.urlopen(req, timeout=20).read().decode(
        "utf-8", errors="ignore"
    )

    if KEYWORD in html:
        if not already_notified():
            msg = (
                " CONVOCAÇÃO ENCONTRADA!\n\n"
                "HRLN – RESULTADO FINAL E CONVOCAÇÃO\n"
                "TÉCNICO DE TI – 6º LUGAR – 004/2025\n\n"
                "Confira no site oficial."
            )
            send_telegram(msg)
            mark_notified()
        else:
            print("Já notificado.")
    else:
        print("Ainda não saiu.")

if __name__ == "__main__":
    main()
