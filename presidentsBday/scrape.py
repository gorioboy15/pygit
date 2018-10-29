import requests
import json
from bs4 import BeautifulSoup as bs
import re
url = 'https://statesymbolsusa.org/categories/state-capital'
headers = {'user-agent':'Mozilla/5.0 (Linux; Android 4.3; Nexus 7 Build/JSS15Q)'}
r = requests.get(url, headers = headers).text

#print(r.status_code)
#print(r.headers)
#print(r.content)
soup = bs(r, 'html5lib')
#print(soup)
#print(soup.prettify())
# body = soup.body
# for i in body:
#     print(i)
states = [s.text.strip(' ') for s in soup.find_all('div', class_="views-field views-field-title-1")]
capital = [s.text.strip(' ') for s in soup.find_all('div', class_="views-field views-field-title-2")]

stcp = {k:v for k,v in zip(states,capital)}
print(stcp)

# with open('stcp.text','w') as f:
#     json.dump(stcp, f)
#

