import sys
print "hello"
try:
	print "next is exit"
	sys.exit(1)
except SystemExit:
	print "SystemExit Exception Handling"
	pass
print "there"

