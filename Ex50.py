soma = 0
for c in range(0,6):
    n = int(input('Digite o número: '))
    if n%2==0:
        soma+=n
print('A soma dos pares digitados é {}'.format(soma))