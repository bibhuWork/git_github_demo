#!/home/myfamily/anaconda3/bin/python

myStr1='Bibu'
myStr2='Subu'

print ('Plain Simple Way : ' + myStr1 + '<->' + myStr2)

print ('Using sep Keyword : ' )
print ( myStr1 , myStr2 , sep= ' <-> ')

print ('C++ printf way : names are %s and %s ' %(myStr1,myStr2))

print ('Using format 1: names are {0} and {1}' .format(myStr1 , myStr2))
print ('Using format 2: names are {1} and {1}' .format(myStr1 , myStr2))
print ('Using format 3: names are {1} and {0}' .format(myStr1 , myStr2))
print ('Using format 4: names are {1} and {2}' .format(myStr1 , myStr2,"SuBi"))

print ('Right justified : %30s ' %('Hi How are you ?'))
print ('R justified : %30s ' %('I am doing Ok'))


print ('R justified : %10d ' %(10000))
print ('R justified : %10d ' %(1000000))

print ('Left justified : %-30s ' %('Hi How are you ?'))
print ('L justified : %-30s ' %('I am doing Ok'))


print ('L justified : %-10d ' %(10000))
print ('L justified : %-10d ' %(1000000))
