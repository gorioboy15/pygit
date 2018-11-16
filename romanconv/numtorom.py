l=[1,4,5,9,10,40,50,90,100,400,500,900,1000]
d={1:'I',4:'IV',5:'V',9:'IX',10:'X',40:'XL',50:'L',90:'XC',100:'C',400:'CD',500:'D',900:'CM',1000:'M'}
samp=1
res=''
i1=0
l.reverse()
#go =
#while go
for i in l:
   if i <= samp:
      res=divmod(samp,i)
      i1=i
      break
print(res)
print(d[i])
