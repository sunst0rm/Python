# This is a script that clicks a belly of puppet clown at pajacyk.pl

#!/usr/bin/env python
import requests

url = 'http://pajacyk.pl//api/clicks'
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; XH; rv:8.578.498) fr, Gecko/20121021 Camino/8.723+ (Firefox compatible)'}

response = requests.post(url, headers=headers)
print(response.json()['count'])
