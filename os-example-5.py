import os
def listall(path):
	for file in os.listdir(path):
		print file	
	print "================="

listall("/home/dengwei/testpsrc")

cwd=os.getcwd()
print cwd
listall(cwd)

os.chdir("/home/dengwei/projects")
print cwd
listall(cwd)

os.chdir(os.pardir)
print cwd
listall(cwd)
