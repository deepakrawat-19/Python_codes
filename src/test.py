i=int(input('enter a no. :'))
p=0
oct=0
while i>0:
    rem=int(i%8)
    i=int(i/8)
    oct=oct + int(rem*pow(10,p))
    p+=1

print(oct)