import requests
import getpass
import json

from requests.structures import CaseInsensitiveDict

def get_token(url, user, pw):
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"

    data = '{{"username": "{user}", "password": "{pw}", "refresh": "token"}}'
    data = data.format(user=user, pw=pw)

    resp = requests.post(url, headers=headers, data=data)

    token_dict = json.loads(resp.text)

    token = token_dict['access_token']
    return token

if __name__ == "__main__":
    url = "http://10.73.26.118:4340/auth/v1/password"
    user = input('Enter hvrhub username: ')
    pw = getpass.getpass()
    print(get_token(url,user, pw))