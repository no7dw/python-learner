import bisect
def index(a,x):
	'locate the leftmost value exactly equal to x'
	i=bisect_left(a,x)
	if i!=len(a) and a[i] ==x:
		return i
	raise ValueError

def find_lt(a,x):
	'find rightmost value less than or equal to x'
	i=bisect_left(a,x)
	if i:
		return a[i-1]
	raise ValueError

def find_le(a,x):
	i=bisect_right(a,x)
	if i:
		return a[i-1]
	raise ValueError

def find_gt(a,x):
	i=bisect_righ(a,x)
	if i!=len(a):
		return a[i]
	raise ValueError

def find_ge(a,x):
	i=bisect_left(a,x)
	if i!=len(a):
		return a[i]
	raise ValueError

def grade(score, breakpoints=[60,70,80,90], grades="FDCBA"):
	i=bisect(breakpoints, score)
	return grades[i]

#print [grade(score) for score in [33,99,77,70,89,90,100]]

