'''
Extracting Data from JSON

In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
'''

import urllib.request, urllib.parse, urllib.error
import json


url = input('Enter - ')
uh = urllib.request.urlopen(url)
data = uh.read().decode()
info = json.loads(data)
num=list()
for items in info.values():
    try:
        for item in items:
            print(item)
            num1=item["count"]
            num1=int(num1)
            num.append(num1)
    except: continue

s=sum(num)
print('Sum=',s)
