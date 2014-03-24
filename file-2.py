import fileinput
import sys
import glob,string

#read the first line and print in uppercase

for line in fileinput.input(glob.glob("./time-1.py")):
	if fileinput.isfirstline():
		sys.stderr.write("-- reading %s --\n" % fileinput.filename())
		sys.stdout.write(str(fileinput.lineno()) + " "+ string.upper(line))
	


