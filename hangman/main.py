#!/usr/bin/python3
''' Hangman program, word 
guessing game'''
from hangman import underscrs # import def that create empty lines to fill in 
from random import choice # pick the word randomly
from word import wrd
l = ['chair','wood','house','cabinet',] 
# words choices 
word = choice(l)
n = l.index(word) # index the word chosen
tot = 0
if '__main__' == __name__:
	template = underscrs(l,n)
	print(*template,sep=' ')
	guess = input('Enter: ')
	word = wrd(guess,word,template)
	print('this is the main')
	print(*word,sep=' ') # print  clean with unpack r sep method
