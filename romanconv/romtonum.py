'''Convert roman numerals to decimals '''

d={'I':1,'IV':4,'V':5,'IX':9,'X':10,
  'XL':40,'L':50,'XC':90,'C':100,
  'CD':400,'D':500,'CM':900,'M':1000}



def romtodec(r):
    rom = r.upper()
    r1, ck = 0, 0
    s, e = 0, 2 # for slicing
    if len(rom) > 1: # check len of roman input
        for r in rom: # loop if it's greater than 1
            if ck == 0:
                if rom[s:e] in d.keys(): # check if it has double roman numerals(e.g iv,ix etc.)
                    r1 += d[rom[s:e]] # add the double numerals
                    s += 1 # update slice for next loop
                    e += 1 # update slice for next loop
                    ck = 1  # update to skip the next loop
                elif r in d.keys():
                    r1 += d[r]
                    s += 1
                    e += 1
            else:
                ck = 0
                s += 1
                e += 1
                continue
        return r1

    else:
        if rom in d.keys():
            return d[rom]

while True:
    rs = input('enter: ')
    print(romtodec(rs))
