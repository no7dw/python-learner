import os
###############################

fp=open("./testdir/testfile","w+")
fp.write("inspector praline")
fp.close()

os.remove("./testdir/testfile")
os.removedirs("./testdir")

