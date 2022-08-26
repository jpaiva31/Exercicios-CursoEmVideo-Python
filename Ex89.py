lista = []
n = ' '
while n not in 'Nn':
    aux = []
    aux.append(str(input('Nome: ')))
    aux.append(float(input('Nota 1: ')))
    aux.append(float(input('Nota 2: ')))
    lista.append(aux[:])
    n = str(input('Quer continuar? [S/N] '))
    while n not in 'NnSs':
        n = str(input('Comando inválido! Quer continuar? [S/N] '))
print("""-=-=-=-==-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-==-=
No. Nome        Média   
---------------------------""")
for c in range(0,len(lista)):
    print('{}  {}            {}'.format(c,lista[c][0],(lista[c][1]+lista[c][2])/2))
id = 0
while id != 999:
    id = int(input('Mostrar notas de qual aluno?'))
    print('Notas de {} são {}'.format(lista[id][0],lista[id][1:]))