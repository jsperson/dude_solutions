import getpass
import hvr_login
url = "http://10.73.26.118:4340/auth/v1/password"
user = input('Enter hvrhub username: ')
pw = getpass.getpass()
print(hvr_login.get_token(url,user, pw))