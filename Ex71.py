n = int(input('Que valor você quer sacar?'))
c1=c2=c3=c4=c5=0
while n>0:
    while n>=50:
        c1+=1
        n=n-50
    while n>=20:
        c2+=1
        n=n-20
    while n>=10:
        c3+=1
        n=n-10
    while n>=5:
        c4+=1
        n=n-5
    while n>=1:
        c5+=1
        n=n-1
if c1!=0:
    print('Total de {} cédulas de 50'.format(c1))
if c2!=0:
    print('Total de {} cédulas de 20'.format(c2))
if c3!=0:
    print('Total de {} cédulas de 10'.format(c3))
if c4!=0:
    print('Total de {} cédulas de 5'.format(c4))
if c5!=0:
    print('Total de {} cédulas de 1'.format(c5))