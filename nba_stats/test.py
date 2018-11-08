with open('nba_names.txt','r')as nbanames:
   nba_names = nbanames.read()
#for n in nba_names:
n= nba_names.split(',')
print(n)
print(type(nba_names)) 
