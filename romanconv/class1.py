l=[1,4,5,9,10,40,50,90,100,400,500,900,1000] # test numbers
d={1:'I',4:'IV',5:'V',9:'IX',10:'X',40:'XL',50:'L',90:'XC'
    ,100:'C',400:'CD',500:'D',900:'CM',1000:'M'}
l.reverse() # check l backwards

d1={'I':1,'IV':4,'V':5,'IX':9,'X':10,'XL':40,'L':50,'XC':90,'C':100,
    'CD':400,'D':500,'CM':900,'M':1000}

'''Convert decimal numbers to roman numerals'''

class Roman:
    def dectorom(self,n):
        if n.isdigit():
            num = int(n)
            cnt = []
            for i in l:  # loop the list to test numbers
                if i <= num:  # i must be lower or equal to the decimal input
                    res = divmod(num, i)  # get quotient and mod
                    i1 = i
                    if res[0] >= 1 and res[1] == 0:  # check if no mod
                        if res[0] == 1:
                            cnt.append(d[i1])
                            break
                        else:
                            for i in range(res[0]):
                                cnt.append(d[i1])
                            break
                    elif res[0] >= 1 and res[1] > 0:
                        if res[0] == 1:
                            cnt.append(d[i1])
                            if res[1] != 0:
                                num = res[1]
                            else:
                                break
                        else:
                            for i in range(res[0]):
                                cnt.append(d[i1])
                            if res[1] != 0:
                                num = res[1]
                            else:
                                break
            return ''.join(cnt)
        else:
            return 'Must be integer'





    '''Convert roman numerals to decimals '''

    def romtodec(self,r):
        rom = r.upper()
        r1, ck = 0, 0
        s, e = 0, 2 # for slicing
        if len(rom) > 1: # check len of roman input
            for r in rom: # loop if it's greater than 1
                if ck == 0:
                    if rom[s:e] in d.keys(): # check if it has double roman numerals(e.g iv,ix etc.)
                        r1 += d1[rom[s:e]] # add the double numerals
                        s += 1 # update slice for next loop
                        e += 1 # update slice for next loop
                        ck = 1  # update to skip the next loop
                    elif r in d1.keys():
                        r1 += d1[r]
                        s += 1
                        e += 1
                else:
                    ck = 0
                    s += 1
                    e += 1
                    continue
            return r1

        else:
            if rom in d1.keys():
                return d1[rom]