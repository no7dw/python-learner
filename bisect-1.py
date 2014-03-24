import bisect
list=[1,2,3,4,6,7,8,9]
print bisect.bisect_left(list, 5)
print list

print bisect.bisect_right(list, 5)
print bisect.bisect(list,5)
bisect.insort_left(list, 5, 0, len(list))
print list

bisect.insort_right(list, 5)
print list
