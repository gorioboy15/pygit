import requests
from bs4 import BeautifulSoup as bs
url = 'http://www.indepthinfo.com/articles/presidential-birthdays.shtml'
# for android mobile headers
#headers = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Mobile Safari/537.36'
# for chrome windows headers
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
res = requests.get(url, headers = headers).text
#print(res.status_code)
soup = bs(res, 'lxml')
#print(soup.prettify())
td = ''
pres = []
table = soup.find('table', border="0", cellspacing="0", cellpadding="2")
for tr in table.find_all('tr'):
    for td in tr.find_all('td'):
        pres.append(td.text)
pres_bday = [ s.strip('\n ') for s in pres ]
#us_president_bday = { k:v for k,v in pres_bday }
#print(us_president_bday)
print(pres_bday)


#print(table)

