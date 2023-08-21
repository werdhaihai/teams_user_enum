import json
import requests
from urllib.parse import unquote, parse_qs

# These Cookies can be retireved from an authenticated session using the Team web app
skypetoken_asm = ""
authtoken = ""

# Read emails from emails.txt
with open('emails.txt', 'r') as f:
    emails = f.read().splitlines()

# Prepare the json
final_json = {
    'emails': emails,
    'phones': []
}


decoded_str = unquote(authtoken.replace('+', '%2B'))
query_string = parse_qs(decoded_str)
bearer = query_string.get('Bearer', [None])[0]


# Set the headers
headers = {
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/json;charset=utf-8',
    'X-Skypetoken': skypetoken_asm,
    'Authorization': "Bearer " + bearer
}


# Make the POST request
response = requests.post(
    'https://teams.live.com/api/mt/beta/users/searchUsers',
    headers=headers,
    json=final_json
)

# Output the response for debugging
if response.status_code == 200:
    json_data = response.json()
    for key, value in json_data.items():
        status = value.get('status', "No Status Found")
        if status == 'Success':
            print(key + ":Valid")
        else:
            print(key + ":NotValid")
