#!/usr/bin/python

'''generate letter weak passwd''' 
from random import *
def weak():
	cons = 'bcdfghjklmnpqrstvwxyz'
	vows = 'aeiou'
	strnum='12' # determine if cons or vows
	strngP=[] # build 10 passwd upper and lower
	for i in range(8):
		if not strngP:
			if choice(strnum) == '1':
				st=choice(cons) 
				strngP.append(st)
			else:
				st=choice(vows)
				strngP.append(st)
		else:
			if strngP[-1] in cons:
				st=choice(vows)
				strngP.append(st)
			else:
				st=choice(cons)
				strngP.append(st)
	return ''.join(strngP)


