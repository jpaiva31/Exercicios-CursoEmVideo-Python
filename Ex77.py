tupla = ('APRENDER','PROGRAMAR','LINGUAGEM','PYTHON','CURSO','GRATIS','ESTUDAR','PRATICAR','TRABALHAR','MERCADO','PROGRAMADOR','FUTURO')
for c in tupla:
    print('Na palavra {} temos'.format(c),end=' ')
    for j in c.lower():
        if j == 'a':
            print('a',end=' ')
        if j == 'e':
            print('e',end=' ')
        if j == 'i':
            print('i',end=' ')
        if j == 'o':
            print('o',end=' ')
        if j == 'u':
            print('u',end=' ')
    print('\n')