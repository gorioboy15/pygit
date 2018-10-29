#import json
#import re
from rE import findBday,findNamedef # import two def findBday and findNamedef from rE.py


print('Program to find out Celebrities Birthdays')
print()
print('''You can enter only a name or the whole name.\n''')
print('''Press 1 if you know the whole name.
Press 2 if you only know the first name.''')
#TODO:add random celebs birthday
while True:

    nme = input('Enter here: ')
    if nme == '1':
        findName=input('Enter the complete name: ')
        print()
        print(findBday(findName))

    elif nme == '2':
        nme = input('Enter only the name: ')
        print()
        print(findNamedef(nme))
        yn = input('Try again? y/n: ')
        if yn.lower() == 'yes' or yn.lower() == 'y':
            continue
        else:
            break

