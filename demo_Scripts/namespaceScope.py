#!/home/myfamily/anaconda3/bin/python

myStr1='Hi I am Global'

def myFunction1():
	myStr1='Inside myFunction1'
	print('Inside Function1 and after assigning value : %s' % myStr1)
	def myFunction1_1():
		myStr1='Inside myFunction1_1'
		print('Inside Function1_1 and after assigning value : %s' % myStr1)
		return
	myFunction1_1()
	print ('After calling myFunction1_1() %s' % myStr1)
	return

print ('Before calling myFunction1() %s' % myStr1)
myFunction1()
print ('After calling myFunction1() %s' % myStr1)

print ('----------------------------------------')
myStr1='Hi I am Global'

def myFunction2():
	global myStr1
	myStr1='Inside myFunction2'
	print('Inside Function2 and after assigning value : %s' % myStr1)
	def myFunction2_1():
		myStr1='Inside myFunction2_1'
		print('Inside Function2_1 and after assigning value : %s' % myStr1)
		return
	myFunction2_1()
	print ('After calling myFunction2_1() %s' % myStr1)
	return

print ('Before calling myFunction2() %s' % myStr1)
myFunction2()
print ('After calling myFunction2() %s' % myStr1)

print ('----------------------------------------')
myStr1='Hi I am Global'

def myFunction3():
	myStr1='Inside myFunction3'
	print('Inside Function3 and after assigning value : %s' % myStr1)
	def myFunction3_1():
		nonlocal myStr1
		myStr1='Inside myFunction3_1'
		print('Inside Function3_1 and after assigning value : %s' % myStr1)
		return
	myFunction3_1()
	print ('After calling myFunction3_1() %s' % myStr1)
	return

print ('Before calling myFunction3() %s' % myStr1)
myFunction3()
print ('After calling myFunction3() %s' % myStr1)


print ('----------------------------------------')
myStr1='Hi I am Global'

def myFunction4():
	myStr1='Inside myFunction4'
	print('Inside Function4 and after assigning value : %s' % myStr1)
	def myFunction4_1():
		global myStr1
		myStr1='Inside myFunction4_1'
		print('Inside Function4_1 and after assigning value : %s' % myStr1)
		return
	myFunction4_1()
	print ('After calling myFunction4_1() %s' % myStr1)
	return

print ('Before calling myFunction4() %s' % myStr1)
myFunction4()
print ('After calling myFunction4() %s' % myStr1)
