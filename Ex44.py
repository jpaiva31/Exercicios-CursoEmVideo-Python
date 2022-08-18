n = float(input('Digite o preço das compras: '))
n2 = int(input(""""Defina a forma de pagamento: 
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x no cartão\n"""""
))
if n2==1:
    print("O valor das compras ficou {}".format(n-n*0.1))
elif n2==2:
    print("O valor das compras ficou {}".format(n-n*0.05))
elif n2==3:
    print("O valor das compras ficou {}".format(n))
elif n2==4:
    print("O valor das compras ficou {}".format(n+n*0.2))