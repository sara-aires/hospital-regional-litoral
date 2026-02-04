import os
import urllib.request
import urllib.parse

URL = "https://isgsaude.org.br/hrln/trabalhe-conosco/"
LAST_FILE = "encontrado.txt"

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

TARGET_TEXT = (
    "HRLN – RESULTADO FINAL E CONVOCAÇÃO – "
    "TÉCNICO DE TI 4º LUGAR 004-2025"
)

def send_telegram_message(text: str):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = urllib.parse.urlencode({
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text
    }).encode("utf-8")

    req = urllib.request.Request(url, data=data, method="POST")
    with urllib.request.urlopen(req, timeout=20) as resp:
        resp.read()

def already_notified() -> bool:
    return os.path.exists(LAST_FILE)

def mark_as_notified():
    with open(LAST_FILE, "w") as f:
        f.write("ok")

def fetch_page() -> str:
    req = urllib.request.Request(
        URL,
        headers={
            "User-Agent": "Mozilla/5.0",
            "Accept-Language": "pt-BR,pt;q=0.9"
        }
    )
    with urllib.request.urlopen(req, timeout=20) as resp:
        return resp.read().decode("utf-8", errors="replace")

def main():
    print(">>> Monitor HRLN iniciado")

    html = fetch_page()

    if TARGET_TEXT in html:
        print(">>> TEXTO ENCONTRADO")

        if already_notified():
            print(">>> Já notificado antes, não enviando novamente")
            return

        send_telegram_message(
            "!!!!!! ATENÇÃO!!!!!!!!!!\n\n"
            "Saiu a convocação Hospital Regional:\n\n"
            f"{TARGET_TEXT}"
        )
        mark_as_notified()
        print(">>> Notificação enviada")
    else:
        print(">>> Ainda não saiu o 6º lugar")

if __name__ == "__main__":
    main()
