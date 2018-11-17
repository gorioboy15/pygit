'''Convert decimal numbers to roman numerals'''


l=[1,4,5,9,10,40,50,90,100,400,500,900,1000] # test numbers
d={1:'I',4:'IV',5:'V',9:'IX',10:'X',40:'XL',50:'L',90:'XC'
    ,100:'C',400:'CD',500:'D',900:'CM',1000:'M'}
l.reverse() # check l backwards


def dectorom(n):
      if not n.isalpha():
         num = int(n)
         i1 = 0
         res = ''
         cnt=[]
         # if num == 0:
         #    print('Invalid entry')
         #    break # stop the program if input is 0
         for i in l: # loop the list to test numbers
            if i <= num:
               res=divmod(num,i)
               i1=i
               if res[0] >= 1 and res[1] == 0:
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

while True:
   nu = input('enter: ')
   print(dectorom(nu))