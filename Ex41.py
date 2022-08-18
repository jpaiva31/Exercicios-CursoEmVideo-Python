n = int(input('Digite o ano de nascimento: '))
print('O atleta tem {} anos'.format(2022-n))
if 2022-n<=9:
    print('O atleta é MIRIM!')
elif 2022-n<=14:
    print('O atleta é INFANTIL!')
elif 2022-n<=19:
    print('O atleta é JUNIOR!')
elif 2022-n<=25:
    print('O atleta é SENIOR!')
else:
    print('O atleta é MASTER!')