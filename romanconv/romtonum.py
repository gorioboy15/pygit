'''Convert roman numerals to decimals '''

d={'I':1,'IV':4,'V':5,'IX':9,'X':10,
  'XL':40,'L':50,'XC':90,'C':100,
  'CD':400,'D':500,'CM':900,'M':1000}



def romtodec():
    r1 = 0
    ck = 0
    s=0
    e=2
    rom  = input('convert to  decimal: ').upper()
    if len(rom) > 1:
        for r in rom:
            if ck == 0: 
                if rom[s:e] in d.keys():
                    r1 += d[rom[s:e]]
                    s += 1
                    e += 1
                    ck = 1 
                elif r in d.keys():
                    r1 += d[r]
                    s += 1
                    e += 1
                    ck = 0
            else:
                ck = 0
                s += 1
                e += 1
                continue
        return r1

    else:
        if rom in d.keys():
            
            return d[rom]

#print(romtodec())

        '''
            if res[0] >= 1 and res[1] == 0:
               if res[0] == 1:
                  cnt.append(d[i1])
                  break
               else:
                  #cnt.append(d[i1])
                  for i in range(res[0]):
                     cnt.append(d[i1])
                  break
            elif res[0] >= 1 and res[1] > 0:
               if res[0] == 1:
                  cnt.append(d[i1])
                  if res[1] != 0:
                     samp = res[1]
                  else:
                     break
               else:
                  for i in range(res[0]):
                     cnt.append(d[i1])
                  if res[1] != 0:
                     samp = res[1]

                  else:
                     break
        '''
      #return r1
print(romtodec())
