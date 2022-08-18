n1 = float(input('Digite o primeiro segmento: '))
n2 = float(input('Digite o segundo segmento: '))
n3 = float(input('Digite o terceiro segmento: '))
if(n1+n2>n3 and n1+n3>n2 and n2+n3>n1):
    print('Os 3 segmentos acima podem formar um triangulo!')
else:
    print('Os 3 segmentos acima nao podem formar um triangulo!')