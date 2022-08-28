lista = []
n = ' '
while n not in 'Nn':
    Pessoa = {}
    Pessoa['Nome']= str(input('Nome: '))
    Pessoa['Sexo']= str(input('Sexo: [M/F]'))
    Pessoa['Idade']=int(input('Idade: '))
    lista.append(Pessoa.copy())
    n = str(input('Deseja continuar? [S/N]'))
    if n not in 'SsNn':
        n = str(input('Comando inválido! Deseja continuar? [S/N]'))
media=0
mulheres = []
for c in range(0,len(lista)):
    media+=lista[c]['Idade']
    if lista[c]['Sexo'] in 'Ff':
        mulheres.append(lista[c]['Nome'])
media=media/len(lista)
print("""-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
A) Ao todo temos {} pessoas cadastradas.
B) A média de idade é de {} anos.
C) As mulheres cadastradas foram {}
d) Lista das pessoas que estão acima da média:""".format(len(lista),media,mulheres))
for c in range(0,len(lista)):
    if lista[c]['Idade']>media:
        print('{}'.format(lista[c]))
