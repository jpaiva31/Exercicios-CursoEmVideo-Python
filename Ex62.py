print('Gerador de PA!\n-=-=-=-=-=-=-=-=-=-=-=-=')
n1 = int(input('Primeiro termo: '))
n2 = int(input('Digite a razão da PA: '))
n3=10
tot=0
while n3!=0:
    tot+=n3
    c = 0
    while c < n3:
        print('{}'.format(n1), end=' -> ')
        n1 = n1 + n2
        c += 1
    print('PAUSA')
    n3 = int(input('Quantos termos mais você quer?'))
print('Progressão finalizada com {} termos mostrados!'.format(tot))
