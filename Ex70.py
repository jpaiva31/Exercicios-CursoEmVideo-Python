print("""----------------------------------
        LOJA SUPER BARATÃO
----------------------------------
""")
nome = ' '
precotot = 0
preco = 0
n = ' '
barato = ' '
precin = 0
caro = 0

while n not in 'Nn':
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    if n== ' ':
        barato = nome
        precin = preco
    n = str(input('Quer continuar? [S/N] '))
    if n in 'SsNn':
        precotot+=preco
        if preco<precin:
            barato = nome
            precin = preco
        if preco>1000:
            caro+=1
    else:
        print('COMANDO INVÁLIDO! ')
print("""O total da compra foi R$ {}
Temos {} produtos custando mais de R$ 1000,00
O produto mais barato foi a {} que custa R$ {}""".format(precotot,caro,barato,precin))