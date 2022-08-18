n = int(input('Digite um número inteiro: '))
n2= int(input('Escolha uma das bases para conversão:\n[1] converter para BINÁRIO\n[2] converter para o OCTAL\n[3] converter para HEXADECIMAL\n'))
if n2==1:
    print('{}'.format(bin(n)[2:]))
elif n2==2:
    print('{}'.format(oct(n)[2:]))
elif n2==3:
    print('{}'.format(hex(n)[2:]))