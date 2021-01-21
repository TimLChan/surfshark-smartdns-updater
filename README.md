# Surfshark smartDNS Updater

Updates the allowed IP for the Surfshark SmartDNS service to your current device's public IP. Useful for people who have dynamic IPs that change frequently.

Script created for both Python and Bash. The script stores the public IP address `ss_ipfile.dat` in the temp directory for the last successful update.

## Usage

Current recommendation is to use either script. Both scripts compare the previous IP and the current IP before making the update call to SurfShark's API.

### Python

1. In your python/virtualenv run `pip install -r requirements.txt`
2. Add your Surfshark username and password in one of two ways:
    - **Preferred** - Set environment variables `export SHARK_USERNAME="email@example.com"` and `export SHARK_PASSWORD="password"`
    - Update `sharkConfig.py.example` with your Surfshark username and password
3. Rename `sharkConfig.py.example` to `sharkConfig.py`
4. Run command `python3 surfshark.py` to update Surfshark SmartDNS IP

### Bash

1. Add your Surfshark username and password in one of two ways:
    - **Preferred** - Set environment variables `export SHARK_USERNAME="email@example.com"` and `export SHARK_PASSWORD="password"`
    - Update lines 3 and 4 in `surfshark.sh` with your username (look for `email@example.com`) and password ( look for `password`)
2. Run `chmod +x surfshark.py`
3. Run `./surfshark.py` or `bash surfshark.sh`

## Notes

- The python script only works with Python 3.
- Both scripts can be run using crontab, a really good tool to generate the crontab line is [crontab-generator](https://crontab-generator.org/)

## Questions

- Your code is garbage/needs work/can be improved
  - Please raise an issue, or if you can fix it, send me a pull request!

- I have an idea!
  - Raise an issue and I'll check on it

## Thanks

Thanks to piermark for adding in a way to compare IP addresses before running the update call in issue [#2](https://github.com/TimLChan/surfshark-smartdns-updater/issues/2)
