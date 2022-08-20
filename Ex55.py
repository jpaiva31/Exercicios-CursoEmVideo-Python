for c in range(0,5):
    peso=float(input('Digite o peso da {}º pessoa: '.format(c+1)))
    if c==0:
        menor=peso
        maior=peso
    elif peso>maior:
        maior=peso
    elif peso<menor:
        menor=peso
print('O maior peso lido foi de {}Kg\nO menor peso lido foi de {}Kg'.format(maior,menor))