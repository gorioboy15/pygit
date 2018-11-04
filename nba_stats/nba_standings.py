import requests
from bs4 import BeautifulSoup
import time
headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

with open('nba_stat.txt', 'w') as f:
    f.write('NBA_ASSIST_STATS\n')
num = 1
while num < 280:
    url = 'http://www.espn.com/nba/statistics/player/_/stat/assists/sort/avgAssists/count/{}'.format(num)
    response = requests.get(url, headers = headers)
    if response.status_code == 200:
        time.sleep(1)
        soup = BeautifulSoup(response.text, 'html.parser')
        table_stat = soup.find_all('table', class_='tablehead')
        table_stat = table_stat[0]
        with open('nba_stat.txt','a') as f:
            for row in table_stat.find_all('tr'):
                for cell in row.find_all('td'):
                    f.write(cell.text.ljust(26))
                f.write('\n')
    else:
        print('No response {}'.format(num))
    num += 40
#print(type(table_stat))



