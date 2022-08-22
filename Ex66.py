n = soma = cont =0
while n!= 999:
    n = int(input('Digite um valor (999 PARA PARAR): '))
    if n==999:
        break
    soma+=n
    cont+=1
print('A soma dos {} valores foi de {}!'.format(cont,soma))