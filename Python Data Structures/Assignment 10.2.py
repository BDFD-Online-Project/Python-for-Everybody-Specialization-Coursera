'''
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
'''

fname=input("Enter file name: ")
fh = open(fname)
counts=dict()
for line in fh:
    if not line.startswith("From "):
    	continue
    line=line.split()
    l=line[5]
    l=l[:2]
    counts[l]=counts.get(l,0)+1
tmp=list()
for k,v in counts.items():
	tmp.append((k,v))
	tmp=sorted(tmp)

for k,v in tmp:
	print(k,v)
