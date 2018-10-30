#!/usr/bin/python3
from random import *
l = ['jacket', 'write', 'justify', 'jungle']
try:
	while True:
		wrd = choice(l)
		cnt=l.index(wrd)
		lstwrd = list(wrd)
		shuffle(lstwrd)
		print('Welcome to Jumble Word!\n')
		print(''.join(lstwrd))
		print('\nYou have only one try, good luck!')
		ans = input('Enter here: ')
		if ans  == wrd:
			l.remove(wrd)
			print(l)
			print('You win!')
		else:
			print('You loose!')

except IndexError as e:
	print('bye')
	print(e)

