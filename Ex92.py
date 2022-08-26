cadastro = {}
cadastro['Nome']=str(input('Nome: '))
cadastro['idade']=2022-int(input('Data de Nascimento: '))
cadastro['ctps']=str(input('Carteira de trabalho (0 não tem) '))
if cadastro['ctps']!='0':
    cadastro['Contratação']=int(input('Ano de contratação: '))
    cadastro['Salário']= float(input('Salário: '))
    cadastro['Aposentadoria']= 30-(2022-cadastro['Contratação']+cadastro['idade'])

for c,v in enumerate(cadastro):
    print('-{} tem o valor {}'.format(v, cadastro['{}'.format(v)]))