from random import randint
def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end=' ')
    for c in range(0,5):
        numero = randint(0,10)
        print(numero, end=' ')
        lista.append(numero)
    print('PRONTO!')

def somaPar(lista):
    soma = 0
    for c in range(0,len(lista)):
        if lista[c]%2==0:
            soma +=lista[c]
    print('Somando os valores pares de {}, temos {}'.format(lista,soma))
lista = []
sorteia(lista)
somaPar(lista)
