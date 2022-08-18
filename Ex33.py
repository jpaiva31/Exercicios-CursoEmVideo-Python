n1= int(input('Primeiro valor: '))
n2= int(input('Segundo valor: '))
n3= int(input('Terceiro valor: '))
if n1<n2:
    if n1<n3:
        menor=n1
        if n2>n3:
            maior=n2
        else:
            maior=n3
    else:
        menor=n3
        maior=n2
elif n2<n1:
    if n2<n3:
        menor=n2
        if n1>n3:
            maior=n1
        else:
            maior=n3

    else:
        menor=n3
        maior=n1
print('O menor numero digitado foi {}\nO maior numero digitado foi {}'.format(menor, maior))