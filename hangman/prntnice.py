#!/data/data/com.termux/files/usr/bin/python
l = ['__','__']
def niceprnt(lst):
	l1 =[]
	s=''
	for i in l:
		print(i,end=' ')

l1=[x for x in l]
print(*l1,sep=' ')
