lista = [[],[],[]]
for i in range(0,3):
    for j in range(0,3):
        lista[i].append(int(input('Digite um valor para a posição [{},{}]: '.format(i,j))))
for c in range(0,3):
    print('{}'.format(lista[c]))