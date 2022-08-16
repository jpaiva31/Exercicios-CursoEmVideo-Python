n = str(input('Digite seu nome completo: ')).strip()
aux = n.split()
print('Seu nome em maiúsculas é: {}\nSeu nome em minusculas é: {}\nSeu primeiro nome tem {} letras'.format(n.upper(), n.lower(),len(aux[0])))