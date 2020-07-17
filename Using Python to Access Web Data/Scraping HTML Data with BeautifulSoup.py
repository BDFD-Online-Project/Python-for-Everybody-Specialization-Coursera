'''
Scraping Numbers from HTML using BeautifulSoup In this assignment you will write a Python program similar to http://www.py4e.com/code3/urllink2.py. The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

slist=list()
v=0
tags = soup('span')
for tag in tags:
    tag=tag.decode().split()
    num1=tag[1]
    x=re.findall('[0-9]+',num1)
    for num in x:
        if num==None:
            continue
        else:
    	    v=v+1
    	    num=int(num)
    	    slist.append(num)
s=sum(slist)
print('Sum=',s)
