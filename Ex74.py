import random
maior=0
menor=0
tupla = (random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10))
print('Os valores sorteados foram : ')
for c in range(0,10):
    print('{}'.format(tupla[c]),end=' ')
    if c==0:
        maior=tupla[0]
        menor=tupla[0]
    else:
        if tupla[c]>maior:
            maior=tupla[c]
        if tupla[c]<menor:
            menor=tupla[c]
print('O maior numero sorteado foi {} e o menor {}'.format(maior,menor))