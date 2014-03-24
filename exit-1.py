import os, sys

try:
	print "next exit 1"
	sys.exit(1)
except SystemExit,value:
	print "caught exit(%s)" % value

try:
	os._exit(2)
except SystemExit,value:
	print "caught exit(%s)" % value

print "bye!"

