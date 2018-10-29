import json
import re
#rslt = ''
#n = 0
scelbs = {}

#nme = ''
#namebday=''
with open('celbs.text', 'r')as f: # open the text file using json(dictionary)
    scelbs = json.load(f) # load json to python dictionary

def findNamedef(name): #find it by name if doesnt know the lastname
    morename = []
    ''' Enter a name and it will 
find : How many have names and the lastnames'''
    celbs = str(scelbs)  # convert dictionary to string for regex
    result = re.findall(name + '\s(\w+)\s?(\w+)?', celbs, re.I)  # find last name of the match variable
    bool(result)
    if not result:
        rslt = 'Invalid name entry'
    elif len(result) == 1:
        result1 = re.findall('(\w+)\s?', str(result), re.I)  # with flag ignorecase
        result1.insert(0, name.title())  # insert the name at 0 position
        rslt = '{}'.format(' '.join(result1))  # to join the name and last name and print as a string
        print('Are you looking {}?'.format(rslt))
        print(rslt)
        yn = input('Yes or No: ')
        if yn.lower() == 'yes':
            print()
            rslt = findBday(rslt)
        else:
            rslt =  "Sorry it's the only name on file."
    elif len(result) > 1:  # if more than one name in file
        result1 = str(result)
        result1 = re.findall(r'([a-zA-Z]{1,})+', result1, re.I) ## to filter last names
        print(result1)
        for i in result1:
            morename.append('{} {}'.format(name.title(), i))
        print('There are {} names of {} on file!'.format(len(result),name.title()))
        print(', '.join(morename))
        print()
        reslt = input('Enter the complete name you want: ')
        rslt = findBday(reslt)
    return rslt

def findBday(findName): #find birhtday of the celebrity name
    countfindname = 0
    n = len(scelbs)
    for k, v in scelbs.items():
        n -= 1  # counting down the dict length
        if findName.lower() == k.lower():  # whatever they input it will like caseignorethe string would be lower
            countfindname += 1
            resltbday = '{} was born on {}'.format(k, scelbs[k])  # pull the item and print with the birthday
            n += 1 #  add 1, so for loop won't be down to zero if name found, and stop printing the else.
        elif n == 0:
            if countfindname == 0:
                resltbday = findNamedef(findName)
            elif countfindname == 1:
                resltbday = resltbday
        else:
            continue
    return resltbday




#TODO: find by last name


match = input('Enter: ')
print(findBday(match))
