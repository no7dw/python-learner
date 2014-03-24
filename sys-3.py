import sys

def exitfunc():
	print "world"

sys.exitfunc=exitfunc

print "hello"
sys.exit(1)

print "there" #this is never printed

