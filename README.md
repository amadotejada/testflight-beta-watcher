# testflight-beta-watcher

I enjoy testing various macOS/iOS beta apps via Apple's [TestFlight](https://developer.apple.com/testflight/) program.


Apple currently caps the beta users to 10k, which led me to create this tool. This script checks TestFlight beta apps and alert you when there's open slots for a given list of apps. 

<img src="/notification.png">

####Prepare TestFlight apps
Search online for the app TestFlight invitation URL and extactt the code.

E.g. [Slack](https://slack.com/beta/ios) TestFlight invitation URL is:
 `https://testflight.apple.com/join/QE3kgqJ2`

```json
apps = {
    "Slack": "QE3kgqJ2",
    "Discord": "gdE4pRzI",
    "ProtonMail": "8SxXknzD",
    "1Password": "8SxXknzD",
    "GitHub": "8SxXknzD",
}
```

#### Notifications
In the script for notificatons I'm using the [Pushover](https://pushover.net) but theres many alternatives.

In `send_push_alert()`:
* Enter the user api token
* Enter the app api token


#### Run

Setup a service or cron to run the script at am interval

E.g.:
`0 */6 * * * python3 testflight-beta-watcher.py`

##
#### Disclaimer

This software {testflight-beta-watcher} has not been endorsed or supported by Apple or Pushover and is in no way associated with them and/or its subsidiaries or affiliate.
