lista=[]
for c in range(0,5):
    lista.append(int(input('Digite um valor para a Posição {}:'.format(c))))
    if c==0:
        menor=lista[0]
        maior=lista[0]
    if lista[c]>maior:
        maior=lista[c]
    if lista[c]<menor:
        menor=lista[c]
print('Você digitou os valores {}'.format(lista))
print('O maior valor digitado foi {} na posicao '.format(maior),end='')
for cont,c in enumerate(lista):
    if c==maior:
        print('{} '.format(cont), end='')
print('\nO menor valor digitado foi {} na posicao '.format(menor),end='')
for cont,c in enumerate(lista):
    if c==menor:
        print('{} '.format(cont), end='')
