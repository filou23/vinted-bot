import requests
import time

WEBHOOK = "https://discord.com/api/webhooks/1498045226823188540/66bJUH2q5GwGC38fh409TrS1hQYEPmVFyupT0aXXleEVyu8MsDKzZnPwvMxyljlE2U4s"
VINTED_USER = "289788311-mikekronoss"

seen = set()

def get_page():
    url = f"https://www.vinted.fr/member/{VINTED_USER}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    return requests.get(url, headers=headers).text

while True:
    page = get_page()

    # ⚠️ version simplifiée (on améliore après si tu veux)
    items = page.split("item")

    for item in items:
        if item not in seen:
            seen.add(item)

            title = "🆕 Nouvel item Vinted"
            price = "Prix non détecté"
            link = f"https://www.vinted.fr/member/{VINTED_USER}"

            requests.post(WEBHOOK, json={
                "content": f"{title}\n💰 {price}\n🔗 {link}"
            })

    time.sleep(60)
