lista = []
cont = 0
exp = str(input('Digite a expressão: '))
for c in range(0,len(exp)):
    if exp[c] in '[{(':
        lista.append(exp[c])
    elif exp[c] in ']})':
        if len(lista)==0:
            cont+=1
        else:
            numero = lista.pop()
            if exp[c]=='}':
                if numero!='{':
                    cont+=1
            if exp[c]==']':
                if numero!='[':
                    cont+=1
            if exp[c]==')':
                if numero!='(':
                    cont+=1
if cont==0 and len(lista)==0:
    print('Pode')
else:
    print('Nao pode')