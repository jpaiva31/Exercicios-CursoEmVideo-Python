import random
a = random.randint(0,2)
n = int(input("""""Escolha sua opção:
[0] PEDRA
[1] PAPEL
[2] TESOURA
Qual sua jogada? """""))
if n==a:
    print('Empate!')

else:
    if n==0:
        if a==1:
            print('Você perdeu, eu escolhi papel!')
        else:
            print('Você ganhou, eu escolhi tesoura!')
    elif n==1:
        if a==0:
            print('Você ganhou, eu escolhi pedra!')
        else:
            print('Você perdeu, eu escolhi tesoura!')
    elif n==2:
        if a==1:
            print('Você ganhou, eu escolhi papel!')
        else:
            print('Você perdeu, eu escolhi pedra!')