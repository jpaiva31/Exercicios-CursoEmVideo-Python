n = ' '
lista = []
while n not in 'Nn':
    aux = []
    aux.append(str(input('Nome: ')))
    aux.append(float(input('Peso: ')))
    lista.append(aux[:])
    n = str(input('Deseja continuar? [S/N] '))
    while n not in 'SsNn':
        n = str(input('Comando inválido! Deseja continuar? [S/N] '))
peso = []
peso2 = []
for c in range(0,len(lista)):
    if c==0:
        maior=lista[0][1]
        peso.append(lista[0][0])
        menor=lista[0][1]
        peso2.append(lista[0][0])
    else:
        if lista[c][1]>maior:
            maior=lista[c][1]
            peso.clear()
            peso.append(lista[c][0])
        elif lista[c][1]==maior:
            peso.append(lista[c][0])
        if lista[c][1]<menor:
            menor = lista[c][1]
            peso2.clear()
            peso2.append(lista[c][0])
        elif lista[c][1]==menor:
            peso2.append(lista[c][0])
print("""Ao todo, você cadastrou {} pessoas.
O maior peso foi de {}Kg.Peso de {}
O menor peso foi de {}Kg. O menor peso foi de {}""".format(len(lista),maior,peso,menor,peso2),end='')
