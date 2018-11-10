import csv
import re
names = ''
stat=''
heads = ''
with open('heads.txt','r')as h:
   heads = h.read()
with open('nba_names.txt', 'r') as n:
   names = n.read()
with open('nba_standings_stat.txt','r')as f:
   stat = f.read()

pat = re.compile(r'[0-9\-\.WL]+')
res = re.findall(pat,stat)
cnt = 14
ct = 0
fin = []
f = []
snf = ''
for i in res:
   ct += 1
   if ct != cnt:
      f.append(i)
   elif ct == cnt:
      fin.append(f)
      cnt += 13
      f = []
      f.append(i)
cnt = 0
nf=[]
n  = names.split(',')
#print(n)
#print(fin)
'''for i in fin:
   i.insert(0,n[cnt])
   cnt+=1
for i in fin:
   #print(' '.join(i))
   nf.append(' '.join(i))
'''
#snf = str(nf)
with open('team_stats.txt','r') as reader:
    snf = reader.read()
  # for i in reader:
#       print(nf)

#print(len(fin[0][3])) # print it in order and aligned
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


cnt = 0
heads = heads.strip(',')
heads = heads.split(',')
names = names.split(',')
for stat in fin:# insert team names at the start(index 0) of every stats list
   stat.insert(0,names[cnt])
   cnt += 1

print(heads)
#print(names)
print(fin)
with open('nba_stats.csv', 'w')as csvfile:
   nba_stats = csv.writer(csvfile)
   nba_stats.writerow(heads)
   for stats in fin:
      nba_stats.writerow(stats)



