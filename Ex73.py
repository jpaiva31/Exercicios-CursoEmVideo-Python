br = ('Palmeiras','Fluminense','Flamengo','Corinthians','Internacional','Athletico-PR','Atlético-MG','Santos','América-MG','Bragantino','Goiás','São Paulo','Fortaleza','Botafogo','Ceará','Cuiabá','Avaí','Coritiba','Atlético-GO','Juventude')
print("""==================================
        TABELA BRASILEIRAO
==================================""")
n = 0
while n != 6:
    n=int(input("""Escolha uma opção!
1- Mostrar a tabela
2- Mostrar os 5 primeiros
3- Mostrar os 4 últimos
4- Mostrar times por ordem alfabética
5- Procurar um time específico
6- Sair\n"""))
    if n == 1:
        for cont,c in enumerate(br):
            print('{}: {}'.format(cont+1,c))
    elif n == 2:
        for c in range(0,5):
            print('{}: {}'.format(c+1,br[c]))
    elif n == 3:
        for c in range(-4,0):
            print('{}: {}'.format(c+21,br[c]))
    elif n == 4:
        for cont,c in enumerate(br):
            print('{}: {}'.format(cont+1,sorted(br)[cont]))
    elif n == 5:
        time = str(input('Digite o time que você quer saber a posicao: ')).upper()
        cont=0
        for cont,c in enumerate(br):
            if c.upper()==time:
                print('O {} está na {} posicao'.format(c,cont+1))
        if cont == 19:
            print('O time digitado não está no brasileirão!')