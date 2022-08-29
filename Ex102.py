def fatorial(n,show=False):
    for c in range(n,0,-1):
        if show==True:
            if c==1:
                print('1 =',end=' ')
                break
            print('{}'.format(c),end=' x ')
        if c==1:
            break
        n*=c-1
    return n

print(fatorial(5,True))
