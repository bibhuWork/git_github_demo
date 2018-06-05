#!/home/myfamily/anaconda3/bin/python

myInt1 = int(input('Enter 1st input : '))
myInt2 = int(input('Enter 2nd input : '))

if( myInt1 == myInt2 ):
	print ('First input is same Second input ' + repr(myInt1))
elif( myInt1 > myInt2 ):
	print ('First input ' +  repr(myInt1) + ' is greater than Second input ' +  repr(myInt2))
else:
	print ('First input ' + repr(myInt1) + ' is less than Second input ' + repr(myInt2))
