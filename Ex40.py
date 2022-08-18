n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
print('Tirando {} e {}, a média do aluno é {}'.format(n1,n2,(n1+n2)/2))
if (n1+n2)/2>=7:
    print('O aluno está aprovado!')
else:
    print('O aluno está reprovado!')