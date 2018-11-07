import json
import re
from random import choice
scelbs = {}


with open('celbs.text', 'r')as f: # open the text file using json(dictionary)
    scelbs = json.load(f) # load json to python dictionary
scelbs1 = {k:v[0:4] for k,v in scelbs.items()} # dict comprehention - filter only what year they are born

celbs = str(scelbs1)  # convert dictionary to string for regex
def findName(name): #find it by name if doesnt know the lastname
    ''' Enter a name and it will
    search for it. You can search full, first, middle and last,
    and even the first few letters in dict file   '''
    result = re.findall(r'[\s?a-zA-Z\s?]+[\s?a-zA-Z\-?]+[\s+-?]+' + name + r'[?=\s?\-?\w+]+', celbs,re.I)  # find middle name of the match var
    if not result:
      result = re.findall(r'[\w+\w+]*' + name + r'[\s?a-zA-Z]+[\-?\w+]*[\s?\w+]+' , celbs, re.I) # find first name of the match var
      if not result:
       result = re.findall(r'[\s?a-zA-Z\s?]+[\s?a-zA-Z-?]+[\w+\s?\.?]+' + name, celbs, re.I)  # find last name of the match variable
       if not result:
         result = 'Nothing on file'
    return result

def fullNameBday(fname):
  ''' finds the fname var birthday'''
  r = [k for k in scelbs1.keys() if fname.lower() == k.lower()]
  #for k in scelbs1.keys(): # search the dict file for fname
   # if fname.lower() == k.lower(): # if found, ignores case
  if r:
    res = '{} was born on {} '.format(''.join(r),scelbs1[''.join(r)]) # print the fname with birth date in string format
  else:
    res = 'Invalid entry'
    #  return res
  #else:
    #res = fname # if fname not found in dict file
    #res = 'Invalid entry'
  return res



while True: # START THE PROGRAM
    randchoice = choice([s for s in scelbs.keys()]) # list comprehention and random choice to print random birthdays
    print('Did you know! {} '.format(fullNameBday(randchoice)))
    match = input('Enter name here: ') # enter the celebrity name that you look for birthday
    fNB = fullNameBday(match) # call the def for birthday lookup
    fN = findName(match) # call def(regex) to filter name. if you don't know the full name
    if fNB != 'Invalid entry':
        print(fNB)
    elif fNB == 'Invalid entry': # if name not found fNB def
        if fN == 'Nothing on file':
            print(fN)
        elif len(fN) > 1: # count how many name in fn def
            print('We found {} names on file:'.format(len(fN)))
            print(', '.join(fN)) # print out names to choose from
            #print(fN)
            name = input('Type the complete name you want: or type n ')
            for nam in fN:
                if name == 'n' or name == '':
                    print('Ok, try again!')
                    break
                elif nam.lower() == name.lower():
                    res = fullNameBday(name)  # insert name in birthday lookup def
                    print(res)
                    break
            else:
                print(fullNameBday(name))

        elif len(fN) == 1: # only a name
            print(''.join(fN))
            print('Is this the name you are looking for? y/n')
            yn = input('Enter y or n: ')
            print()
            if yn.lower() == 'y' or yn.lower() == ''.join(fN).lower():
                print(fullNameBday(''.join(fN))) # call birthday lookup def
            else:
                print('Ok, try again!')






#print(fNB)
#print(fN)