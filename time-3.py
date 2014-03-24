import time
now=time.localtime(time.time())
print "asctime",time.asctime(now)
print "ymd HM",time.strftime("%y/%m/%d %H:%M", now)
print "abd",time.strftime("%a %b %d", now)
print "c",time.strftime("%c", now)
print "Ip",time.strftime("%I %p", now)
print "Ymd HMs Z",time.strftime("%Y-%m-%d %H:%M:%s %Z", now)

year, month, day, hour, minute, second, weekday, yearday, daylight = now
print "040202d","%04d-%02d-%02d" % (year, month, day)
print "040202d","%04d-%02d-%02d" % (hour, minute, second)
print ("MON","TUE","WED","THU","FRI","SAT","SUN")[weekday],yearday, daylight
