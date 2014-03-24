import time
now=time.time()
print now, "seconds since", time.gmtime(0)[:6]
print
print "or in other words:"
print "- local time:", time.localtime(now)
print "- local time.tm_mday:", time.localtime(now).tm_mday
print "- utc:", time.gmtime(now)

