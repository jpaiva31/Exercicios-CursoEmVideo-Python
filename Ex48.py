soma=0
cont=0
for c in range(0,501):
    if c%2!=0:
        if c%3==0:
            soma+=c
            cont+=1
print('A soma dos {} valores solicitados é {}'.format(cont,soma))