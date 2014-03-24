import string
import os
for path in string.split(os.environ["PATH"], os.pathsep):
	print path

print os.environ["USER"]
