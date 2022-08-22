tot = 0
cont = 0
c=' '
while c not in 'N':
    n = int(input('Digite um número: '))
    tot+=n
    if cont==0:
        maior=n
        menor=n
    elif n>maior:
        maior=n
    elif n<menor:
        menor = n
    c= str(input('Quer continuar? [S/N]'))
    if c not in 'NnSs':
        while c not in 'SsNn':
            c=str(input('Comando inválido! Digite S/N'))
    cont+=1
print('Você digitou {} números e a média foi {}'.format(cont,float(tot/cont)))
print('O maior valor foi {} e o menor foi {}!'.format(maior,menor))