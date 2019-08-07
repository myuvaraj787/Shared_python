class circlr:
	def __init__(self,r):
		self.rad = r
	def area(self,rad):
		return self.rad**2*3.14


r=float(input('enter value'))
a=circlr(r)
print (a.area(r))



