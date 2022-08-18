n = float(input('Digite o salário do funcionario: '))
if n<1250:
    print('O novo salário desse funcionario é {}'.format(n+n*0.15))
else:
    print('O novo salário desse funcionario é {}'.format(n + n * 0.10))