#!/bin/sh

surfshark_username=surfshark@username.com
surfshark_password=mypassword
login_payload_template='{"username":"%s","password":"%s"}'
login_payload=$(printf "$login_payload_template" "$surfshark_username" "$surfshark_password")

echo "Initialising Surfshark SmartDNS Updater v1.0"
echo "Logging in with username $surfshark_username"

login_request=`curl -s -X POST "https://api.surfshark.com/v1/auth/login" -H "Content-Type: application/json" --data $login_payload`
if [ -z "$login_request" ]
then
    echo "Login failed. Check your username or password"
    exit 1
else
    bearer_token=`echo $login_request | awk -F "[,:}]" '{print $2}' | tr -d '"'`
    echo "Logged in successfully"
fi

update_request=`curl -s -X POST "https://api.surfshark.com/v1/server/smart-dns" -H "Authorization: Bearer $bearer_token"`
user_ip=`echo $update_request | awk -F "[,:}]" '{print $4}' | tr -d '"'`

if [ "$user_ip" = "Invalid JWT Token" ]
then
    echo "Update failed - Payload $update_request"
    exit 1
else
    echo "Updated SmartDNS IP to $user_ip"
fi