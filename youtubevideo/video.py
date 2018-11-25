import requests
from bs4 import BeautifulSoup
import re
scrape_url = 'https://www.youtube.com/results?search_query='
search_var = 'web+scraping+with+python'
headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
url = scrape_url + search_var

r = requests.get(url, headers=headers)
page = r.text
href=[]
soup = BeautifulSoup(page,'lxml')
#print(soup.prettify())
#yt = soup.find_all('a', {'href':re.compile('/watch?v=[a-zA-Z0-9_\-]+')})
yt = soup.find_all("a")
for a in yt:
    print(a)



print(len(yt))

# for x in yt_link:
#     print(x.get('href'))


