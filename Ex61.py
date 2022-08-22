print('Gerador de PA!\n-=-=-=-=-=-=-=-=-=-=-=-=')
n1 = int(input('Primeiro termo: '))
n2 = int(input('Digite a razão da PA: '))
c=0
while c<10:
    print('{}'.format(n1),end=' -> ')
    n1=n1+n2
    c+=1
print('FIM')