import UserDict
class Add(UserDict.UserDict):
	def __init__(self, dict = {}, **kwargs):
		UserDict.UserDict.__init__(self)
		self.update(dict)
		self.update(kwargs)
	def __add__(self, other):
		dict = Add(self.data)
		dict.update(other)
		return dict

a=Add(a=1)
b=Add(b=2)
print a+b
