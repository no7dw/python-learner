import mmap
import os, string, re

def mapfile(filename):
	file=open(filename,"r+")
	size=os.path.getsize(filename)
	return mmap.mmap(file.fileno(), size)

data=mapfile("./123.txt")

#search
index=data.find("small")
print index, repr(data[index-5:index+15])


