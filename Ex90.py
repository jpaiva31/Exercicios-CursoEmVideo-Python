cadastro = {}
cadastro['Nome']=str(input('Nome: '))
cadastro['Media']=float(input('Média de {}: '.format(cadastro['Nome'])))
if cadastro['Media']>=7:
    cadastro['Situacao']= 'Aprovado'
elif cadastro['Media']>=5:
    cadastro['Situacao'] = 'Recuperaçao'
else:
    cadastro['Situacao'] = 'Reprovado'
print("""-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    -Nome é igual a {}
    -Média igual a {}
    -Situação é igual a {}""".format(cadastro['Nome'],cadastro['Media'],cadastro['Situacao']))