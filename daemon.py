import os,time
pid =os.fork()
if pid:
	print "next _exit0"
	os._exit(0) #kill original

print "daemon started"
time.sleep(5)
print "daemon terminated"

