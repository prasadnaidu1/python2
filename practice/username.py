username=input('enter the username:')
password=input('enter the password')
if username.startswith('prasad') and password.endswith('.com'):
    print('username and password are matched')
else:
    print('username and password not matched')