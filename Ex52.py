qtd=0
n = int(input('Digite um número: '))
for c in range(1,n):
    if n%c==0:
        qtd+=1
if qtd>2:
    print('O número não é primo!')
else:
    print('O número é primo!')