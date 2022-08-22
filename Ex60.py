n = int(input('Digite um número para calcular seu fatorial: '))
fat=n
print('Calculando {}! = '.format(n),end='')
while n!=0:
    if n==1:
        print('{} = {}'.format(n,fat))
    else:
        print('{}'.format(n), end=' x ')
    n-=1
    fat*=n
if fat==0:
    print('0')
