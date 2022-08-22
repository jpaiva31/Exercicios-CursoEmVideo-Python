n = str(input('Informe seu sexo: [M/F] ')).strip()[0]
while n not in 'MmFf':
    n= str(input('Comando invalido! Informe seu sexo: [M/F] '))
    print('{}'.format(n))
print('Sexo {} Registrado com sucesso! '.format(n))