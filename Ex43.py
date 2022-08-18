n1 = float(input('Digite o peso: '))
n2 = float(input('Digite a altura: '))
imc = n1/(n2*n2)
print('O IMC desta pessoa é de {}'.format(imc))
if imc<18.5:
    print('Essa pessoa está ABAIXO do nível normal!')
elif imc<25:
    print('Essa pessoa está com o IMC IDEAL!')
elif imc<30:
    print('Essa pessoa está UM POUCO ACIMA do nível normal!')
elif imc<40:
    print('Essa pessoa está com o IMC BEM ACIMA do nível normal!')
else:
    print('Essa pessoa está ABSURDAMENTE ACIMA do nível normal!')