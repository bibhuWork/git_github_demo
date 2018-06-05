#!/home/myfamily/anaconda3/bin/python

class MyClass():
	a=0
	b=0
	c=0
	def __init__(self):
		print('Hello MyClass')
	def assignValue(self,x,y):
		self.a=x
		self.b=y
		print ('a and b are %d %d' %(self.a,self.b))
	def addVar(self):
		self.c=self.a+self.b
	def printSum(self):
		print ('Sum is %d' %self.c)

class mySubClass(MyClass):
	def __init__(self):
		print ('Hello Sub Class')

mc = MyClass()
mc.assignValue(5,9)
mc.addVar()
mc.printSum()

print('-----------------------------')

msc = mySubClass()
msc.assignValue(12,15)
msc.printSum()

print('-----------------------------')
	
class MyClass1():
	def __init__(self,p,q):
		print('Hello MyClass1')
		self.a=p
		self.b=q
	def assignValue(self):
		print ('a and b are %d %d' %(self.a,self.b))
	def addVar(self):
		self.c=self.a+self.b
	def printSum(self):
		print ('Sum is %d' %self.c)

class mySubClass1(MyClass1):
	def __init__(self):
		print ('Hello Sub Class1')

mc = MyClass1(13,14)
mc.assignValue()
mc.addVar()
mc.printSum()

print('-----------------------------')

msc = mySubClass1()
msc.assignValue() 
# We will get error as we are trying to print a & b which are non existant as sub class donit funct in sub class and not main classn't cAL
