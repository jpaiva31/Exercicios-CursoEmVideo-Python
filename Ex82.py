lista =[]
par = []
impar =[]
n= ' '
while n not in 'Nn':
    lista.append(int(input('Digite um valor: ')))
    n = str(input('Deseja continuar? [S/N] '))
    if n not in 'SsNn':
        n = str(input('Comando inválido! Deseja continuar? [S/N] '))
for c in range(0,len(lista)):
    if lista[c]%2==0:
        par.append(lista[c])
    else:
        impar.append(lista[c])
print('A lista completa é {}\nA lista de pares é {}\nA lista de ímpares é {}'.format(lista,par,impar))
