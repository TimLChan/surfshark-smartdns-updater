import json
import requests
import base64
import tempfile
import os
import sharkConfig as config
from datetime import datetime

req = requests.session()
oldip = "0.0.0.0"
filename = os.path.join(tempfile.gettempdir(), config.TEMPFILE_NAME)

# Get old IP from temp file if exists
if os.path.exists(filename):
    with open(filename, 'r') as f:
        oldip = f.read()

# Write updated IP to temp file if changed
def writetmpfile(ip):
    with open(filename, "w") as f:
        f.write(ip)

def logmessage(msg):
    print(('[{}] {}').format(datetime.now().strftime('%Y-%m-%d %I:%M:%S %p'), msg))

# Compares current IP to previous IP to see if surfshark smartDNS IP address needs to be updated or not
def needupdate():
    try:
        currentip = req.get(config.IP_API).text
        logmessage('Current IP: {} | Previous IP: {}'.format(currentip, oldip))
        if currentip != oldip:
            return True
        else:
            return False
    except:
        logmessage("Couldn't get current IP - updating DNS IP anyway")
        return True

def main():
    logmessage('Initialising Surfshark SmartDNS Updater v2.0')
    if needupdate():

        # Prefer using environment variables over hardcoded variables in config file
        surfsharkusername = os.environ.get('SHARK_USERNAME') if os.environ.get('SHARK_USERNAME') is not None else config.SHARK_USERNAME
        surfsharkpassword = os.environ.get('SHARK_PASSWORD') if os.environ.get('SHARK_PASSWORD') is not None else config.SHARK_PASSWORD
        loginpayload = config.SHARK_LOGIN_PAYLOAD.format(surfsharkusername, surfsharkpassword)

        # Make a call to the SurfShark login API to get a bearer token for smartDNS update call
        logmessage('Logging in with username {}'.format(surfsharkusername))
        try:
            login = req.post(config.SHARK_LOGIN_URL, data=loginpayload, headers={'Content-Type': 'application/json'})
            loginjson = login.json()
            bearertoken = loginjson["token"]
            logmessage('Logged in successfully')
        except:
            logmessage('Login failed. Check your username or password')
            exit(1)
        
        # Make a POST call to with the bearer token to activate smartDNS for the current IP
        logmessage('Sending request to update SmartDNS')
        try:
            update = req.post(config.SHARK_UPDATE_URL, headers={'Authorization': 'Bearer {}'.format(bearertoken)})
            update = update.json()
            logmessage('Updated SmartDNS IP to {}'.format(update["ip"]))
            writetmpfile(update["ip"])
        except:
            logmessage('Update failed - Payload: {}'.format(update))
    else:
        logmessage('No update required, exiting')

if __name__ == "__main__":
    main()
