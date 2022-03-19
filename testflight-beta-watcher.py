import os

import requests

home = os.path.expanduser("~")
url = "https://testflight.apple.com/join/"
apps = {
    "Slack": "QE3kgqJ2",
    "Discord": "gdE4pRzI",
    "ProtonMail": "8SxXknzD",
    "1Password": "8SxXknzD",
    "GitHub": "8SxXknzD",
}


def check_beta():
    for app, code in apps.items():
        tmpfile = f"{home}/.{app}"
        print(f"Checking: {app} beta")
        resp = requests.get(f"{url}/{code}")
        if resp.ok:
            if "beta is full" in resp.text:
                if os.path.isfile(tmpfile):
                    os.remove(tmpfile)
            else:
                if not os.path.isfile(tmpfile):
                    send_push_alert(app, code, url)
                    open(tmpfile, "a").close()
        else:
            print(f"\n{app} not found, {resp.status_code}")


def send_push_alert(app, code, url):
    resp = requests.post(
        "https://api.pushover.net/1/messages.json",
        data={
            "token": "{}",
            "user": "{}",
            "message": f"{app} Beta is available!\n{url+code}",
        },
    )
    print(resp.text)


check_beta()
