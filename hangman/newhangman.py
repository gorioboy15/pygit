#!/usr/bin/python3
''' Hangman program, word 
guessing game'''
from hangman import underscrs # import def that create empty word template to fill in 
from random import choice # pick the word randomly
import os
from word import wrd
l = ['chair','wood','house','cabinet',]  
w = choice(l) # words chosen
n = l.index(w) # index the word chosen
tot = 0
cnt=0
guess=len(w)-1 #  how many guesses allowed 
r = underscrs(l,n) # calling def underscrs to get the word template
clear = os.system('clear')
yes = True
print('Welcome to Word Guessing Game!\n')
print(*r,sep=' ')
print('You got {} letter word {} guesses'.format(len(w),guess))
while yes: # while True
	g = input('Enter: ') # guess letter inuput
	word = wrd(g,w,r) # called def wrd to manipulate def underscrs template
	cnt=word.count(g) # count correct letter from input
	if list(w) == word: 
		os.system('clear')
		print('Welcome to Word Guessing Game!\n')
		print(*word,sep=' ')
		print('You Win!')
		onemore = input('Another game? y/n: ')
		if onemore == 'y':
			os.system('clear')
			l = ['chair','wood','house','cabinet',]  
			w = choice(l) # words chosen
			n = l.index(w) # index the word chosen
			r = underscrs(l,n)
			guess = len(w)-1
			print('Welcome to Word Guessing Game!\n')
			print(*r,sep=' ')
			print('You got {} letter word {} guesses'.format(len(w),guess))
			continue
		else:
			yes = False
	elif cnt != 0: # if there is a correct letter
		os.system('clear')
		print('Welcome to Word Guessing Game!\n')
		print(*word,sep=' ') # unpack var(word) and sep method to print nice and clean
		print('You got {} correct letter'.format(cnt))
	elif cnt == 0: # if there's no correct letter
		os.system('clear')
		print('Welcome to Word Guessing Game!\n')
		print(*word,sep=' ') 
		guess-=1
		if guess != 0:
			os.system('clear') # clear screen
			print('Welcome to Word Guessing Game!\n')
			print(*word,sep=' ')
			print('{} guesses left '.format(guess))
			
		else:
			print('You loose!')
			onemore=input('Another game? y/n: ')

			if onemore == 'y':
				os.system('clear')
				l = ['chair','wood','house','cabinet',]  
				w = choice(l) # words chosen
				n = l.index(w) # index the word chosen
				r = underscrs(l,n)
				guess = len(w)-1
				print('Welcome to Word Guessing Game!\n')
				print(*r,sep=' ')
				print('You got {} letter word {} guesses'.format(len(w),guess))
				continue
			else:
				yes = False

