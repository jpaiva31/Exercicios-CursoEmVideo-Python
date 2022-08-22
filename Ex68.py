import random
vitorias = derrotas=0
print("""
=-=-=-=-=-=-=-=-=-=-=-=-=-
VAMOS JOGAR PAR OU ÍMPAR
=-=-=-=-=-=-=-=-=-=-=-=-=-""")
while derrotas==0:
    n1 = random.randint(0,10)
    n2 = int(input('Diga um valor: '))
    n3 = str(input('Par ou ímpar? [P/I]'))
    print("""
-----------------------------
Você jogou {} e o computador {}. Total de {} DEU """.format(n2,n1,n2+n1),end='')
    if (n1+n2)%2==0:
        if n3 in 'Pp':
            print("""PAR!
-----------------------------""")
            vitorias+=1
            print("""Você venceu!
Vamos jogar novamente...
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-""")
        elif n3 in 'Ii':
            derrotas+=1
            print("""PAR!
        Você PERDEU!
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-""")
        else:
            print('\nComando inválido!')
    else:
        if n3 in 'Ii':
            print("""IMPAR
-----------------------------""")
            vitorias += 1
            print("""Você venceu!
Vamos jogar novamente...
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-""")
        elif n3 in 'Pp':
            derrotas += 1
            print("""ÍMPAR!
Você PERDEU!
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-""")
        else:
            print('\nComando inválido!')
print("""=-=-=-=-=-=-=-=--=-=-=-=-
GAME OVER! Você venceu {} vezes!
""".format(vitorias))