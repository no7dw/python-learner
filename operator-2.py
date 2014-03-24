import copy
a=[[1],[2],[3]]
#b=copy.copy(a)
b=copy.deepcopy(a)

print "before","==>"
print a
print b

###mod

a[0][0]=0
a[1]=None
#a[1][0]=None

print "after","==>"
print a
print b

