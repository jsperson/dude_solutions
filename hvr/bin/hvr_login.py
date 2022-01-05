import requests
from requests.structures import CaseInsensitiveDict
import getpass
import json

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
    import params
    url = params.hvr_host_url + params.hvr_host_login_path
    user = input('Enter hvrhub username: ')
    pw = getpass.getpass()
    print(get_token(url,user, pw))