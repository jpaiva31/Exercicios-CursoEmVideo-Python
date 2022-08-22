n=0
cont=0
cont2=0
while n!=999:
    n=int(input('Digite um numero[999 para parar]'))
    if n!=999:
        cont+=n
        cont2+=1
print('Você digitou {} números e a soma deles foi {}!'.format(cont2,cont))