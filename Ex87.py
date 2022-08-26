lista = [[],[],[]]
for i in range(0,3):
    for j in range(0,3):
        lista[i].append(int(input('Digite um valor para a posição [{},{}]: '.format(i,j))))
for c in range(0,3):
    print('{}'.format(lista[c]))
somaPar = 0
soma3 = 0
for i in range(0,3):
    for j in range(0,3):
        if lista[i][j]%2==0:
            somaPar+=lista[i][j]
        if j==2:
            soma3+=lista[i][j]
        if i == 1:
            if j==0:
                maior=lista[i][j]
            else:
                if maior<lista[i][j]:
                    maior=lista[i][j]
print("""A soma dos valores pares é {}
A soma dos valores da terceira coluna é {}
O maior valor da segunda linha é {}""".format(somaPar,soma3,maior))