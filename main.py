import requests
import time

WEBHOOK = "https://discord.com/api/webhooks/1498045226823188540/66bJUH2q5GwGC38fh409TrS1hQYEPmVFyupT0aXXleEVyu8MsDKzZnPwvMxyljlE2U4s"
VINTED_USER = "289788311-mikekronoss"

seen = set()

def check_vinted():
    url = f"https://www.vinted.fr/member/{VINTED_USER}"
    r = requests.get(url)

    # version simple (on améliorera après)
    if "item" in r.text:
        return True
    return False

while True:
    if check_vinted():
        requests.post(WEBHOOK, json={
            "content": "🆕 Nouveau article Vinted détecté !"
        })

    time.sleep(60)
