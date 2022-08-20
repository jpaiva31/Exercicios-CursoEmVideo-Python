cont=0
cont2=0
for c in range(0,4):
    print('====={}º PESSOA====='.format(c+1))
    nome=str(input('Nome:'))
    idade=int(input('Idade: '))
    Sexo=str(input('Sexo [M/F]: '))
    cont+=idade
    if Sexo == 'M' and c==0:
        velho=nome
        idVelho=idade
    elif Sexo == 'M' and idade>idVelho:
        velho=nome
        idVelho=idade
    if Sexo == 'F' and idade<20:
        cont2+=1
print("""A média de idade do grupo é de {} anos
O homem mais velho tem {} anos e se chama {}
Ao todo são {} mulheres com menos de 20 anos""".format(float(cont/4),idVelho,velho,cont2))