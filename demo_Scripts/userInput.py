#!/home/myfamily/anaconda3/bin/python

urName = input('What\'s your name ?')

print (urName)

print ('Welcome Mr. ' + urName )

myIntInput1 = input('Enter First Input : ')
myIntInput2 = input('Enter Second Input : ')

myWrongOutput1 = myIntInput1 + myIntInput2
print ('The sum is :' + (myWrongOutput1) + ' -- Wrong ')

myIntOutput1 = int(myIntInput1) + int(myIntInput2)

print ('The sum is :' + repr(myIntOutput1))
