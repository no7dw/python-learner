import mmap
import os
filename="/home/dengwei/python_test/stand/123.txt"

file=open(filename, "r+")
size=os.path.getsize(filename)
data=mmap.mmap(file.fineno(), size)

#basics
print data
print len(data), size

#use slicing to read from the file
print repr(data[:10]), repr(data[:10])

print repr(data.read(10)), repr(data.read(10))


