jogador = {}
jogador['Nome']= str(input('Nome do jogador: '))
n = int(input('Quantas partidas {} jogou? '.format(jogador['Nome'])))
lista = []
for c in range(0,n):
    lista.append(int(input('Quantos gols na partida {}? '.format(c))))
jogador['gols']=lista[:]
jogador['total']=0
for c in range(0,len(lista)):
    jogador['total']+=lista[c]
print("""-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
{}
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=""".format(jogador))
for c,v in enumerate(jogador):
    print('O campo {} tem o valor {}'.format(v,jogador['{}'.format(v)]))
print("""-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
O jogador {} jogou {} partidas.""".format(jogador['Nome'],n))
for c in range(0,n):
    print('=> Na partida {}, fez {} gols.'.format(c,jogador['gols'][c]))
print('Foi um total de {} gols'.format(jogador['total']))