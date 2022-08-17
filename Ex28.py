import random
n = random.randint(0,5)
f = int(input('Escolha um numero de 0 a 5: '))
if f==n:
    print('Você acertou! O numero certo é: {}'.format(n))
else: print('Você errou! O numero certo era: {}'.format(n))