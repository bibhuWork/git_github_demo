#!/home/myfamily/anaconda3/bin/python

myInt1 = 3
myInt2 = 5

myFloat1 = 3.0
myFloat2 = 5.0


myStr1 = "My Name Is"
myStr2 = "Bibhudatta Sarangi"

print (myInt1 + myFloat1)

# print (myFloat2 + myStr2)
#TypeError: unsupported operand type(s) for +: 'float' and 'str'

print (myStr1 + ' ' + repr(myFloat1))

print (myStr2 + ' ' + repr(myInt2 + myInt1))
