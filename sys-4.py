import sys
import atexit

def exit(*args):
	print "exit func", args

#register two exit handler

atexit.register(exit)
atexit.register(exit,1)
atexit.register, "hello" , "world"

print "there" #this is never printed

exit("hello", "world")
exit(1,);
exit()

