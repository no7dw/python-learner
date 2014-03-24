import UserList
class AutoList(UserList.UserList):
	def __init__(self):
		super(AutoList,self).__init__(self)
	def __setitem__(self, i, item):
		if i==len(self.data):
			self.append(item)
		else:
			self.data[i]=item

list = AutoList()

for i in range(10):
	list[i]=i
print list
