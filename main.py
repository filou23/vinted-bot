import requests
import time
import re

WEBHOOK = "https://discord.com/api/webhooks/1498045226823188540/66bJUH2q5GwGC38fh409TrS1hQYEPmVFyupT0aXXleEVyu8MsDKzZnPwvMxyljlE2U4s"
URL = "https://www.vinted.fr/member/289788311-mikekronoss"

seen = set()

def get_page():
    headers = {"User-Agent": "Mozilla/5.0"}
    return requests.get(URL, headers=headers).text

def extract_links(page):
    # récupère les vrais liens Vinted
    return re.findall(r"/items/\d+", page)

while True:
    page = get_page()
    items = extract_links(page)

    for item in items:
        full_link = "https://www.vinted.fr" + item

        if full_link not in seen:
            seen.add(full_link)

            requests.post(WEBHOOK, json={
                "content": f"🆕 **Nouvel item Vinted**\n🔗 {full_link}"
            })

    time.sleep(60)
