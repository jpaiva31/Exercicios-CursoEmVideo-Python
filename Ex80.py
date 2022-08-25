lista = []
c=0
while c in range(0,5):
    numero = int(input('Digite um valor: '))
    i=0
    while i <len(lista):
        if numero>lista[i]:
            i+=1
        else:
            break
    if i==len(lista):
        if numero not in lista:
            lista.append(numero)
            print('Adicionado ao final da lista!')
        else:
            print('Valor duplicado! Nao adicionarei!')
            c -= 1
    else:
        if numero not in lista:
            lista.insert(i,numero)
            print('Adicionado na posicao {}'.format(i))
        else:
            print('Valor duplicado! Nao adicionarei!')
            c-=1
    c+=1
lista.sort()
print('Os valores digitados em ordem foram {}'.format(lista))