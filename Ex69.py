n = ' '
homens = 0
cont = 0
cont2 = 0
while n not in 'Nn':
    print("""--------------------------------------
    CADASTRE UMA PESSOA
--------------------------------------""")
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]'))
    if sexo in 'MmFf':
        if idade>18:
            cont+=1
        if sexo in 'Mm':
            homens+=1
        elif sexo in 'Ff' and idade<20:
            cont2+=1
    else:
        print('Comando inválidooo!')
    n = str(input('Deseja continuar? [S/N]'))
    if n not in 'SsNn':
        print('Comando inválidu!')
print('Total de pessoas com mais de 18 anos: {}\nAo todo temos {} homens cadastrados\nE temos {} mulheres com menos de 20 anos'.format(cont,homens,cont2))