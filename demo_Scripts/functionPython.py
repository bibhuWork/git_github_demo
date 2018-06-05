#!/home/myfamily/anaconda3/bin/python

myStr1 = 'Su Bi'
myInt1 = 1
myInt2 = 2

def intFunction (myIntInp1=6,myIntInp2=5):
	'A simple function Demo Calling Function By Val'
	myIntInp2=4
	print ("Int value inside function is %d & %d"  % (myIntInp1,myIntInp2))
	return

intFunction(12,13)
print ('Inputs are %d & %d' %(myInt1,myInt2))
intFunction(myInt1,myInt2)
print ('Calling function without any argument')
intFunction()
print ('Calling function with one argument')
intFunction(19)

myInpArry = [2]

def arryFunction(myInpParameter):
	'A simple function Demo Calling Function By Reference'
	print ('Inside Function Before Operation')
	print(myInpParameter)	
	myInpParameter.append(myInpParameter*2)
	print ('Inside Function After Operation')
	print(myInpParameter)	
	return

print ('In main program Before calling function')
print(myInpArry)
arryFunction(myInpArry)
print ('In main program After calling function' )
print(myInpArry)
