class MyClass:
	x = 5
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def myfunc(self,a):
		print("my fucntion",a)
		print("self name",self.name)

p1 = MyClass('john',34)
p1.myfunc('my function')
