import requests
from bs4 import BeautifulSoup
import csv

url = 'http://www.worldometers.info/geography/alphabetical-list-of-countries/'
headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

page = requests.get(url, headers = headers).content
#print(page.status_code)
#print(page.content)
soup = BeautifulSoup(page, 'html.parser')
#print(soup.prettify())
country = soup.find_all('td', style='font-weight: bold; font-size:15px')

countries = [i.text for i in country]
cn = soup.find_all('td', style="font-weight: bold; text-align:right")
population = [a.text for a in cn]
la = soup.find_all('td', style="text-align:right")
land_area = [l.text for l in la if la.index(l) % 2 == 0]
density = [l.text for l in la if la.index(l) % 2 == 1]
result = [[c,p,l,d] for c,p,l,d in zip(countries,population,land_area,density)]
# with open('countries.csv','w')as f:
#     headers = ['Country', 'Population','Land_Area','Density']
#     csv_writer = csv.writer(f)
#     csv_writer.writerow(headers)
#     for r in result:
#         csv_writer.writerow(r)
#







#print(countries)