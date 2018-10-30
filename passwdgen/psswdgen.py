#!/usr/bin/python

'''password generator strong'''
from random import *
num = '0123456789'
chrs = '@_^!~+*$%&-#'
abc = 'abcdefghijklmnpqrstuvwxyz'
strnum='12' # determine if upper,lower,chars and nums
strngP=[]
# build 10 passwd upper and lower
for i in range(10):
	if choice(strnum) == '1':
		strngP.append(choice(abc).upper())
	else:
		strngP.append(choice(abc))

# add numbers and characters to 10 passwd
for i in range(5): 
	if choice(strnum) == '1':
		strngP.append(choice(num))
	else:
		strngP.append(choice(chrs))


print(''.join(strngP))
shuffle(strngP)
print(''.join(strngP))
		 

print('hi')
