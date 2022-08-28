def dizMaior(*lista):
    maior=0
    for c in range(0,len(lista)):
        if c == 0:
            maior=lista[0]
        else:
            if lista[c]>maior:
                maior=lista[c]
    print("""{}
Foram informados ao todo {} valores
O maior valor informado foi {}""".format(lista,len(lista),maior))


dizMaior(2,9,4,5,7,1)
dizMaior(4,7,0)
dizMaior(1,2)
dizMaior(6)
dizMaior()