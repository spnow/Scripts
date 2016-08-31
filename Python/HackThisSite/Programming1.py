#!/usr/bin/env python
from collections import Counter
import getpass
import requests

answer = ""

def validWord(word, letterList):
    word2, word1 = Counter(word), Counter(letterList)
    return all(word2[k] <= word1.get(k, 0) for k in word2)

def getproblem():
    password = getpass.getpass()
    url = "https://www.hackthissite.org/missions/prog/1/"
    login = "https://www.hackthis.co.uk/?login"
    payload = {"username": "dtctd", "password": password}
    s = requests.Session() # Start a session
    s.post(login, data=payload) # Login
    problem = s.get("https://www.hackthis.co.uk/levels/extras/captcha1.php")
    return problem

def solve(problem):


with open('wordlist.txt','r') as f:
    content = f.read().splitlines()
for line in content:
    if len(line) == 6:
        word = validWord(line, ["p", "s", "o", "o", "y", "k"])
        if word:
            answer += line
print answer
