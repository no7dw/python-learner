class Rectangle:
	def __init__(self, color = "white", width=10, height=10):
		print "create a", color, self, "size", width, "x", height

class RoundRectangle(Rectangle):
	def __init__(self, **kw):
		apply(Rectangle.__init__, (self,), kw)

rect = Rectangle(color = "green", height =100, width =100)
rect = RoundRectangle(color = "blue", height=20)
rect = RoundRectangle(color = "blue", width=5)
