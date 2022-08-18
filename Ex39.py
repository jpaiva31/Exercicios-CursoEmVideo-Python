n = int(input('Ano de nascimento: '))
print('Quem nasceu em {} tem {} anos em 2022'.format(n,2022-n))
if 2022-n==18:
    print('Você deve se alistar IMEDIATAMENTE!')
elif 2022-n>18:
    print('Você já deveria ter se alistado há {} anos!\nSeu alistamento foi em {}'.format((2022-n)-18,n+18))
elif 2022-n<18:
    print('Ainda faltam {} anos para seu alistamento!\nSeu alistamento será em {}'.format(18-(2022-n),n+18))