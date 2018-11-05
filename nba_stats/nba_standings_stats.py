import requests
from bs4 import BeautifulSoup

url = 'http://www.espn.com/nba/standings/_/group/league'

headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

response = requests.get(url, headers = headers)
soup = BeautifulSoup(response.content, 'html.parser')
print(soup)




#print(response.content)