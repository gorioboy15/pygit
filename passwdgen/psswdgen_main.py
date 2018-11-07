#!/usr/bin/python
from os import system
from psswdgen_strong import strong
from psswdgen_easy import weak

if __name__ == "__main__":
	system('clear')
	print('''Welcome to Password Generator!\n
Press 1 for weak password.
Press 2 for strong password.''')
	p=input('Enter: ')
	if p is '2':
		print(strong())
	elif p is '1':	
		print(weak())
	else:
		print('Invalid entry')
