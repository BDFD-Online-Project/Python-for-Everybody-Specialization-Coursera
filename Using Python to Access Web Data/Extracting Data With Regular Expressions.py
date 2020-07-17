'''
Finding Numbers in a Haystack

In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.
'''

import re

#fname=input("Enter file name: ")
fh = open("regex_sum_58.txt")
slist=list()
v=0
for line in fh:
    line=line.rstrip()
    x=re.findall('[0-9]+',line)
    for num in x:
    	if num==None:
        	continue
    	else:
        	v=v+1
        	num=int(num)
        	slist.append(num)
s=sum(slist)
print('There are '+str(v)+' values with a sum='+str(s))
