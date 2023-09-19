import os
from datetime import datetime

import pytz
import requests

date = datetime.now(pytz.timezone("America/New_York"))
time12hr = date.strftime("%Y-%m-%d %I:%M:%S %p")

home = os.path.expanduser("~")
url = "https://testflight.apple.com/join/"
apps = {
    "WhatsApp": "s4rTJVPb",
    "Slack": "QE3kgqJ2",
    "Discord": "gdE4pRzI",
    "ProtonMail": "8SxXknzD",
    "1Password": "8SxXknzD",
    "GitHub": "8SxXknzD",
}


def check_beta():
    for app, code in apps.items():
        tmpfile = f"{home}/testflight-beta-watcher.log"
        print(f"\nChecking: {app}")
        resp = requests.get(f"{url}/{code}")
        print(f"Status: {resp.status_code}")
        if resp.ok:
            if "Join the Beta" in resp.text:
                send_push_alert(app, code, url)
                open(tmpfile, "a").write(f"\n{time12hr} -- ✅ Found ✅: {app, url+code}")
            else:
                open(tmpfile, "a").write(f"\n{time12hr} -- ⛔️ Unavailable ⛔️: {app}")


def send_push_alert(app, code, url):
    requests.post(
        "https://api.pushover.net/1/messages.json",
        data={
            "token": "{}",
            "user": "{}}",
            "message": f"✅ {app} Beta is available! ✅\n{url+code}",
        },
    )
    print(f"{time12hr} -- ✅ Found ✅: {app, url+code}")


if __name__ == '__main__':
    check_beta()
