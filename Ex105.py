def notas(*n,sit=False):
    dic = {}
    dic['total'] = len(n)
    dic['maior'] = max(n)
    dic['menor'] = min(n)
    dic['media'] = sum(n)/len(n)
    if sit:
        if dic['media']>=7:
            dic['situacao'] = 'Aprovado'
        else:
            dic['situacao'] = 'Reprovado'
    return dic

resp = notas(5.5,2.5,1.5,sit =True)
print(resp)