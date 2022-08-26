import random
n = int(input("""-------------------------
        MEGA SENA
-------------------------
Quantos jogos você quer que eu sorteie? """))
lista = []
for c in range(0,n):
    jogo = []
    for i in range(0,6):
        jogo.append(random.randint(0,60))
    lista.append(jogo[:])
for c in range(0,n):
    print('Jogo {}: {}'.format(c+1,lista[c]))