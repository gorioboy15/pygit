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
soup = bs(r, 'lxml')
#print(soup)
#print(soup.prettify())

states = []
alam = 'Alabama'
n = 0
for t in soup.find_all('span', class_='field-content'):
    states.append(t.a.text)

print(states.count(70))


