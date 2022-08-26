from  random import randint
import operator
jogador = {'Jogador1':randint(1,6),
           'Jogador2':randint(1,6),
           'Jogador3':randint(1,6),
           'Jogador4':randint(1,6)}
jogador = sorted(jogador.items(), key = operator.itemgetter(1),reverse=True)
print("""-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    == RANKING DOS JOGADORES ==
""")
for i,c in enumerate(jogador):
    print('{}º lugar: {} tirou {} no dado'.format(i+1,c[0],c[1]))