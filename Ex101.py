def voto(ano):
    idade = 2022-ano
    if idade<16:
        return 'Com {} anos, não vota!'.format(idade)
    elif idade<18 or idade>65:
        return 'Com {} anos o voto é opicional!'.format(idade)
    else:
        return 'Com {} anos, o voto é obrigatório!'.format(idade)


print(voto(int(input('Em que ano você nasceu?'))))