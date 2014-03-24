import os
filename="/home/dengwei/test.txt"
print "ext=>", os.path.splitext(filename)
###############################

cwd=os.getcwd()
print "1", cwd

os.chdir("../")
print "2", os.getcwd()

os.chdir(os.pardir)
print "3", os.getcwd()
###############################

