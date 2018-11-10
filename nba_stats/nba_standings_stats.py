import requests
from bs4 import BeautifulSoup

url = 'http://www.espn.com/nba/standings/_/group/league'

headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
response = requests.get(url, headers = headers)
soup = BeautifulSoup(response.content, 'html.parser')
span = soup.find_all('span', class_="hide-mobile")
with open('nba_names.txt','w')as n:
    for i in span:
        #print(i.text + '**')
        n.write(i.text + ',')

# th = soup.find_all('th', class_="tar subHeader__item--content Table2__th")
# with open('heads.txt', 'w')as h:
#     for i in th:
#         h.write(i.text)
#         h.write(',')
#         print(i.text)

with open('nba_standings_stat.txt','w') as f:
    for td in soup.find_all('td', class_="Table2__td"):
        for span in td.find_all('span', class_="stat-cell"):
            f.write(span.text)
        f.write(' ')

#print(soup.prettify)
# print(len(a))f
# print(type(td))




#print(response.content)
