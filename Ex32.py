n = int(input('Digite um ano: '))
bis = False
if(n%4==0):
    if(n%100!=0):
        bis = True
    else:
        if(n%400==0):
            bis = True
if(bis==True):
    print('O ano {} é bissexto'.format(n))
else:
    print('O ano {} não é bissexto'.format(n))