import json
from random import choice
with open('stcp.text','r') as f:
    stcp = json.load(f)
r = choice([c for c in stcp.keys()])
print(f'{stcp[r]} is the capital of {r}.')
fndcap = input("find U.S Capital City, enter: ").title()
if fndcap in stcp.keys():
    print(f'{stcp.get(fndcap)} is the capital of the {fndcap}')
else:
    print(f'There\'s no state named {fndcap} in U.S.A')


