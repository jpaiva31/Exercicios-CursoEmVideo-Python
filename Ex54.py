novo = 0
velho = 0
for c in range(1,8):
    a=int(input('Em que ano a {}º pessoa nasceu? '.format(c)))
    if 2022-int(a)>=18:
        velho+=1
    else:
        novo+=1
print('Ao todo tivemos {} pessoas maiores de idade\nE tivemos {} pessoas menores de idade'.format(velho,novo))