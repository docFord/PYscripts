#!/usr/bin/python

from os import urandom
import string
import random
import requests
import json
from time import sleep

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed(urandom(1024))

url = 'http://XXX/Googledoc/mail.php' #domain removed

names = json.loads(open('names.json').read())
#passes = json.loads(open('pass.json').read())
emails = ['@gmail.com', '@yahoo.com', '@hotmail.com', '@outlook.com', '@live.com', '@fbi.gov', '@gmx.de', '@hope.org', '@redcross.org', '@tx.gov', '@dhs.gov', '@maine.gov', '@whitehouse.gov', '@dhs.gov', '@nasa.gov']

for name in names:
    name_extra = ''.join(random.choice(string.digits))

    username = random.choice(string.ascii_letters) + name.lower() + name_extra + random.choice(emails)
    password = ''.join(random.choice(chars) for i in range (10))
    #password = random.choice(passes)
    otherr = "Sign+in"
    maill = "other"
    # You will need to change the post fields when submitting data
    
    print("sending username %s and password %s" %(username,password))
    x = requests.post(url, allow_redirects=False, data={
    	'Email': username, # or whatever value
    	'mailtype': maill,
    	'other': otherr,
    	'Passwd': password # or whatever value


    })
    #print(x.json)
    sleep(random.randint(2,201))
