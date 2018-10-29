import json
import re
from random import choice
scelbs = {}


with open('celbs.text', 'r')as f: # open the text file using json(dictionary)
    scelbs = json.load(f) # load json to python dictionary
scelbs = {k:v[0:4] for k,v in scelbs.items()}

print(scelbs)