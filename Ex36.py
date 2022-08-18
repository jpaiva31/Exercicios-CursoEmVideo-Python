n1 = float(input('Digite o valor da casa: '))
n2 = float(input('Digite seu salário: '))
n3 = int(input('Em quantos anos deseja pagar? '))

if(n1/12*n3>n2*0.3):
    print('Para pagar uma casa de {} em {} anos, a prestação será de R$ {}\nEmprestimo CONCEDIDO!'.format(n1,n3,n1/(12*n3)))
else:
    print('Para pagar uma casa de {} em {} anos, a prestação será de R$ {}\nEmprestimo NEGADO!'.format(n1,n3,n1/(12*n3)))