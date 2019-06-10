# Surfshark Smartdns Api
Updates the accepted IP for Surfshark's SmartDNS to your current device's public IP. Useful for people who have dynamic IPs that change frequently. Script created for both Python and Bash

## Usage:

##### Python
1. In your python/virtualenv run `pip install -r requirements.txt`
2. Update `sharkConfig.py.example` with your Surfshark username and password
3. Rename `sharkConfig.py.example` to `sharkConfig.py`
4. Run command `python3 surfshark.py` to update Surfshark SmartDNS IP

##### Bash
1. Update `surfshark.sh` with your username and password
2. Run `chmod +x surfshark.py`
3. Run `./surfshark.py` or `bash surfshark.sh`

## Notes:
- The python script only works with Python 3.
- ~~Bash script coming soon (when I get around to id)~~ Done

## Questions:
- Your code is garbage/needs work/can be improved
    - Please raise an issue, or if you can fix it, send me a pull request!

- I have an idea!
    - Raise an issue and I'll check on it