print("""
----------------------
Sequência de Fibonacci
----------------------""")
n = int(input('Quantos termos você quer mostrar?'))
print("""
~~~~~~~~~~~~~~~~~~~~~~
""")
c=0
aux =0
aux2 = 1
while c<n:
    print('{}'.format(aux),end=' -> ')
    aux3=aux
    aux+=aux2
    aux2=aux3
    c+=1
print('FIM')
print("""
~~~~~~~~~~~~~~~~~~~~~~
""")