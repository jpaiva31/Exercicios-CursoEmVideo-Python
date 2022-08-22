import random
n = random.randint(0,10)
n2=11
while n2!=n:
    n2 = int(input('Tente advinhar o numero que escolhi: '))
    if n2!=n:
        if n2<n:
            print('Mais... Tente novamente!')
        else:
            print('Menos... Tente novamente')
print('Parabéns, você acertou! O numero era {}'.format(n))