tupla = ('Borracha',2,'Caderno',15.9,'Caneta',22.3,'Compasso',9.99,'Estojo',25.0,'Lápis',1.75,'Livro',34.9,'Mochila',120.32,'Transferidor',4.2)
print("""--------------------------------------
        LISTAGEM DE PREÇOS
--------------------------------------
""")
for c in range(0,len(tupla)):
    if c%2==0:
        print('{} R$ {}'.format(tupla[c],tupla[c+1]))
