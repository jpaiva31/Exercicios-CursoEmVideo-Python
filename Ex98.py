from time import sleep
def conta(a,b,c):
    print('-='*20)
    print('Contagem de {} a {} de {} em {}'.format(a,b,c,c))
    if a<b:
        while a<b:
            print('{}'.format(a),end=' ')
            sleep(0.5)
            a+=c
        print('FIM')
    else:
        while a>b:
            print('{}'.format(a),end=' ')
            sleep(1)
            a-=c
        print('FIM')
conta(1,10,1)
conta(10,0,2)
print('Agora é sua vez de personalizar a contagem!')
conta(int(input('Inicio: ')),int(input('Fim: ')),int(input('Passo: ')))