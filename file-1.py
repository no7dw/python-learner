import fileinput
import sys

for line in fileinput.input("./time-1.py"):
	sys.stdout.write("-->")
	sys.stdout.write(line)


