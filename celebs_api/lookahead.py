import re
import json
from celebBdayApp import findBday
celbs = {}
name = ''
with open('celbs.text','r') as f:
	celbs = json.load(f)
celbs=str(celbs)
def lastname(findName):
	''' finds name on a 
dictionary converted str 
file'''
	pt = re.compile(r'[(\w+)+(\s+)]*' + findName + r'[(\s?)(\w+)]*',re.I)
	resultName = re.findall(pt,celbs)
	s = findName
	if len(resultName) == 1:
		resultName = '{}'.format(','.join(resultName))
		resultName = resultName
	elif len(resultName) > 1:
		resultName = 'There are {} {} name found, {}'.format(len(resultName),s,','.join(resultName))
	else:
		resultName = 'Nothing on the record.'
	return resultName
while True:
    n=input('enter ' )
    print(lastname(n))
