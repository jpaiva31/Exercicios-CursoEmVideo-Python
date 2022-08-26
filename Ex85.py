lista = [[],[]]
for c in range(0,7):
    n = int(input('Digite o {}o. valor: '.format(c+1)))
    if n%2==0:
        lista[0].append(n)
    else:
        lista[1].append(n)
print("""Os valores pares digitados foram: {}
Os valores ímpares digitados foram: {}""".format(lista[0],lista[1]))