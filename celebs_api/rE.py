import json
import re

scelbs = {}


with open('celbs.text', 'r')as f: # open the text file using json(dictionary)
    scelbs = json.load(f) # load json to python dictionary

celbs = str(scelbs)  # convert dictionary to string for regex
def findName(name): #find it by name if doesnt know the lastname
    print(name)
    result = re.findall(name + r'[?=\s?\-?\w+]+', celbs,re.I)
    return result

r = {k,v for k,v in scelbs.items()}
print(r)

n = input('Enter here ')
print(findName(n))

