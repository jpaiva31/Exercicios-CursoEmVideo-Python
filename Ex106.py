def ajuda(a):
    return help(a)


n = ' '
while n not in 'fim':
    n = str(input('Função ou biblioteca: '))
    ajuda(n)