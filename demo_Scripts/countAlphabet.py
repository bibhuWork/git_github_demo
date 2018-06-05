#!/home/myfamily/anaconda3/bin/python

import string

alphabet = {}

for alpha in string.ascii_letters:
	alphabet[alpha] = 0

print ('Initial Alphabets counts are %s' % alphabet)

inputStr = input('Input a string : ')

print ('Input String is %s ' % inputStr )

for i in range(len(inputStr)):
	done = False
	for alphaKey in alphabet.keys():
		if (inputStr[i] == alphaKey ):
			alphabet[alphaKey]+=1
			done = True
		if done:
			break

print ('Final Alphabets counts are %s' % alphabet)

for alphaKey in sorted(alphabet.keys()):
	if (alphabet[alphaKey] > 0):
		print ('Found Match : %s %d' %(alphaKey , alphabet[alphaKey]))
