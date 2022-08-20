n = str(input('Digite uma frase: ')).strip().upper()
a=n.split()
junto= ''.join(a)
inverso = ''
i=len(junto)-1
for c in range(0,len(junto)):
    inverso+=junto[i]
    i=i-1
if junto==inverso:
    print('Essa frase é um palíndromo!!')
else:
    print('Essa frase não é um palíndromo!')