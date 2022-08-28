listaJog = []
aux = ' '
while aux not in 'Nn':
    jogador = {}
    jogador['Nome']= str(input('Nome do jogador: '))
    n = int(input('Quantas partidas {} jogou? '.format(jogador['Nome'])))
    lista = []
    for c in range(0,n):
        lista.append(int(input('Quantos gols na partida {}? '.format(c+1))))
    jogador['gols']=lista[:]
    jogador['total']=0
    for c in range(0,len(lista)):
        jogador['total']+=lista[c]
    listaJog.append(jogador.copy())
    aux = str(input('Deseja continuar?'))
    if aux not in 'NnSs':
        aux = str(input('Comando inválido!\nDeseja continuar?'))
print("""-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
cod nome                gols                total
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=""")
for c in range(0,len(listaJog)):
    print('{} {}        {}                  {}'.format(c,listaJog[c]['Nome'],listaJog[c]['gols'],listaJog[c]['total']))
j=0
while j!= 999:
    j = int(input("""-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    Mostrar dados de qual jogador? (999 para parar)"""))
    if j === 999:
        break
    print('--LEVANTAMENTO DO JOGADOR {}'.format(listaJog[j]['Nome']))
    for i in range(0,n):
        print('=> Na partida {}, fez {} gols.'.format(i+1,listaJog[j]['gols'][i]))
