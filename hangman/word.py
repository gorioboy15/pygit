#!/usr/bin/python3
#w = 'houhe'
#l = ['_','_','_','_','_']
#from hangman import underscrs

def wrd(inletter,wrdchosen,blnk):
	for i in range(len(wrdchosen)):
		if inletter == wrdchosen[i]:
			blnk[i]=inletter
		else:		
			continue
	return blnk

