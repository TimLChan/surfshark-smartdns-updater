import json
import urllib3
import sharkConfig as config
import base64
from datetime import datetime
urllib3.disable_warnings()

http = urllib3.PoolManager()


def logmessage(msg):
    print(('[{}] {}').format(datetime.now().strftime('%Y-%m-%d %I:%M:%S %p'), msg))


def main():
    logmessage('Initialising Surfshark SmartDNS Updater v1.0')
    loginpayload = config.SS_LOGIN_PAYLOAD.format(config.SS_USERNAME, config.SS_PASSWORD)
    logmessage('Logging in with username {}'.format(config.SS_USERNAME))
    try:
        login = http.request('POST', config.SS_LOGIN_URL, body=loginpayload, headers={'Content-Type': 'application/json'})
        loginjson = json.loads(login.data.decode('utf-8'))
        bearertoken = loginjson["token"]
        logmessage('Logged in successfully')
    except:
        logmessage('Login failed. Check your username or password')
    
    try:
        logmessage('Sending request to update SmartDNS')
        update = http.request('POST', config.SS_UPDATE_URL, headers={'Authorization': 'Bearer {}'.format(bearertoken)})
        update = json.loads(update.data.decode('utf-8'))
        logmessage('Updated SmartDNS IP to {}'.format(update["ip"]))
    except:
        logmessage('Update failed - Payload: {}'.format(update))
if __name__ == "__main__":
    main()
