import time
n = int(input('Digite que numero a contagem regressiva começará: '))
for c in range(n,0,-1):
    print('{}'.format(c))
    time.sleep(1)