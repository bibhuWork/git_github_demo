#!/home/myfamily/anaconda3/bin/python

myIntInp1 = 0

while ( myIntInp1 < 10 ):
	print ('myInt1 loop : %d' % myIntInp1)
	myIntInp1+=1
else:
	print ('while loop Done')

for myIntInp2 in range(0,10):
	print ('myInt2 loop : %d' % myIntInp2)
else:
	print ('for loop Int Done')

arrayProgLang = ['C++' , 'Java' , 'Python' , 'Perl']

for myProgLang in arrayProgLang:
	print ('Prog Lang is %s ' %myProgLang)
else:
	print ('for loop String Done')
