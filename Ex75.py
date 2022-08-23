n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))
tupla = (n1,n2,n3,n4)
print('Você digitou os valores {}'.format(tupla))
print('O valor 9 apareceu {} vezes'.format(tupla.count(9)))
if 3 in tupla:
    print('O valor 3 apareceu na posicao {}'.format(tupla.index(3)))
print('Os valores pares digitados foram ',end=' ')
for c in range(0,4):
    if tupla[c]%2==0:
        print('{}'.format(tupla[c]),end=' ')