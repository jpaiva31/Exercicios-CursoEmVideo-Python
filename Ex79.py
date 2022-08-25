lista = []
n = ' '
while n not in 'Nn':
    numero=int(input('Digite um valor: '))
    if numero in lista:
        print('Valor duplicado, não adicionarei!')
    else:
        lista.append(numero)
        print('Valor adicionado!')
    n = str(input('Deseja continuar? [S/N]: '))
    while n not in 'SsNn':
        n = str(input('Comando inválido! Deseja continuar? [S/N]: '))
print('Valores adicionados: {}'.format(lista))