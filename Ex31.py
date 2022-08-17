n = int(input('Qual é a distância para sua viagem? '))
print('Você está prestes a começar uma viagem de {} kilometros\n '.format(n))
if(n<=200):
    print('E o preco da sua passagem é {}'.format(n*0.5))
else:
    print('E o preco da sua passagem é {}'.format(n*0.45))
