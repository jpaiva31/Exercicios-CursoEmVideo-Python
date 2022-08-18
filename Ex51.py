n1 = int(input('Digite o primeiro termo: '))
n2 = int(input('Digite a razão da PA: '))
for c in range(0,10):
    print('{}'.format(n1), end=' -> ')
    n1+=n2
print('ACABOU')