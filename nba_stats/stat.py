import re

stat=''
with open('nba_standings_stat.txt','r')as f:
   stat = f.read()
pat = re.compile(r'[0-9\-\.WL]+')
res = re.findall(pat,stat)
cnt = 14
ct = 0
fin = []
f = []
for i in res:
   ct += 1
   if ct != cnt:
      f.append(i)
   elif ct == cnt:
      fin.append(f)
      cnt += 13
      f = []
      f.append(i)

'''with 
open('nba_standings_stat.txt','r')as f:
'  stat = f.read()
for i in stat:
  print(i.replace("",'+'),end=' ')
'''

print(fin)
