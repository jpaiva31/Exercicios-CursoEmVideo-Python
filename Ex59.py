n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3=-1
while n3!=5:
    n3=int(input("""
[ 1 ] Somar: 
[ 2 ] Multiplicar:
[ 3 ] Maior: 
[ 4 ] Novos números: 
[ 5 ] Sair do programa: """))
    if n3==1:
        print('Soma de {} e {} é {}!'.format(n1,n2,n1+n2))
    elif n3==2:
        print('A multiplicação de {} e {} é {}!'.format(n1,n2,n1*n2))
    elif n3==3:
        if n1>n2:
            print('O maior entre {} e {} é {}!'.format(n1,n2,n1))
        elif n1<n2:
            print('O maior entre {} e {} é {}!'.format(n1,n2,n2))
        elif n1==n2:
            print('{} e {} são iguais!'.format(n1,n2))
    elif n3==4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
print('Fim do programa!!')