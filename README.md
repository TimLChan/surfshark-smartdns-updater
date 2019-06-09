# Surfshark Smartdns Api
Updates the accepted IP for Surfshark's SmartDNS to your current device's public IP. Useful for people who have dynamic IPs that change frequently.

## Usage:
1. In your python/virtualenv run `pip install -r requirements.txt`
2. Update `sharkConfig.py.example` with your Surfshark username and password
3. Rename `sharkConfig.py.example` to `sharkConfig.py`
4. Run command `python3 surfshark.py` to update Surfshark SmartDNS IP


## Notes:
- The python script probably only works with Python 3.
- Bash script coming soon (when I get around to id)