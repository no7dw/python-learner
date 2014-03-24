import operator
sequence = 1,2,4
print "add","==>", reduce(operator.add, sequence)
print "sub","==>", reduce(operator.sub, sequence)
print "mul","==>", reduce(operator.mul, sequence)
print "concat","==>", operator.concat("spam", "egg")
print "repeat","==>", operator.repeat("spam", 5)
print "reduce lambda" , "==>" ,reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
print "getitem","==>",operator.getitem(sequence, 2)
print "indexOf","==>",operator.indexOf(sequence, 4)
print "sequenceIncludes","==>", operator.sequenceIncludes(sequence, 3)



