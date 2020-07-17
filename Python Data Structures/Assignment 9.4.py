'''
9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
'''

fname = input("Enter file name: ")
fh = open(fname)
counts=dict()
for line in fh:
    if not line.startswith("From "):
    	continue
    line=line.split()
    l=line[1]
    counts[l]=counts.get(l,0)+1

maximum=None
maxword=None
for k,v in counts.items():
	if maximum==None or maximum<v:
		maximum=v
		maxword=k
print(maxword,maximum)
