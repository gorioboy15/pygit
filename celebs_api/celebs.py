
import requests
import json

celb = 'https://celebritybucks.com/developers/birthdays/JSON'
r = requests.get(celb).json() # convert to json
#print(r.status_code)
#print(r.text)
celbdict={}
with open('celbs.text','r')as f:
	celbdict=json.load(f) # load json text file to python dictionary
#print(r)
for name in r['Birthdays']:
    n = name['name']
    d = name['dob']
    if n not in celbdict and d not in celbdict:
        celbdict[n] = d
    else:
        continue
print(len(celbdict))
# print('{}, was born on {}'.format(n,d))
with open('celbs.text', 'w')as f:
    json.dump(celbdict, f)  # put back to json text file
# print(celb)
