import os
import urllib.request

# LINK DO PDF QUE QUER MONITORAR
PDF_URL = (
    "https://isgsaude.org.br/hrln/wp-content/uploads/sites/5/2020/10/HRLN-RESULTADO-FINAL-E-CONVOCACAO-TECNICO-DE-TI-4o-LUGAR-004-2025.pdf"
)

LAST_FILE = "pdf_notified.txt"

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

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

def pdf_exists(url: str) -> bool:
    try:
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "Mozilla/5.0"}
        )
        with urllib.request.urlopen(req, timeout=20) as resp:
            return resp.status == 200
    except Exception as e:
        print(">>> Erro ao verificar PDF:", e)
        return False

def main():
    print(">>> Monitor de PDF iniciado")

    if pdf_exists(PDF_URL):
        print(">>> PDF encontrado!")

        if already_notified():
            print(">>> Já notificado antes")
            return

        # AVISA NO TELEGRAM
        send_telegram_message(
            f"📄 Convocação encontrada!\n\nVeja o PDF:\n{PDF_URL}"
        )

        mark_as_notified()
        print(">>> Notificação enviada")
    else:
        print(">>> PDF ainda não disponível")

if __name__ == "__main__":
    main()
