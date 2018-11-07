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
ie = []

#print(len(fin[0][3]))
for i in fin:
   for e in i:
      if e == i[3] and len(e) == 1:
         i[3] = f'{i[3]}  '
      elif e == i[9] and len(e) == 4:
         i[9] = f'{i[9]} '
      elif e == i[10] and len(e) == 3:
         i[10] = f'{i[10]}  '
      elif e == i[10] and len(e) == 4:
         i[10] = f'{i[10]} '
      else:
         continue
         
      
for i in fin:
   print('  '.join(i))
