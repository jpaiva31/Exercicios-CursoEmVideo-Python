lista = []
n = ' '
while n not in 'Nn':
    lista.append(int(input('Digite um valor: ')))
    n = str(input('Quer continuar? [S/N]'))
    while n not in 'SsNn':
        n = str(input('Comando inválido! Quer continuar? [S/N]'))
print('Você digitou {} elementos!'.format(len(lista)))
lista.sort(reverse=True)
print('Os valores em ordem decrescente são: {}'.format(lista))
if 5 in lista:
    print('O 5 está na lista!')
else:
    print('O 5 não está na lista!')