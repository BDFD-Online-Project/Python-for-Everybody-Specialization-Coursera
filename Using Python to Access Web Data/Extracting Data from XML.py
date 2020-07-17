'''
Extracting Data from XML

In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.
'''

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
tree = ET.fromstring(data)
counts = tree.findall('comments/comment')
num=list()
for line in counts:
    a=line.find('count').text
    a=int(a)
    num.append(a)
s=sum(num)
print('Sum=',s)

#Alternative method:
import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
num=list()
stuff=ET.fromstring(html)
counts = stuff.findall('comments/comment')
for line in counts:
    a=line.find('count').text
    a=int(a)
    num.append(a)
s=sum(num)
print('Sum=',s)
