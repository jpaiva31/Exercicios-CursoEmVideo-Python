def jogador(a,b):
    if a.strip()=='':
        a='<Desconhecido>'
    if b.strip().isnumeric()==False:
        b=int(0)
    return 'O jogador {} fez {} gol(s) no campeonato'.format(a,b)


print(jogador(str(input('Nome do jogador: ')),str(input('Numero de gols: ')) ))
