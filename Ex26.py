n = str(input('Digite uma frase: ')).upper()

print('A letra A aparece {} vezes na frase\nA primeira letra A aparece na posicao {}\nA ultima letra A aparece na posicao {}'.format(n.count('A'),n.find('A'),n.rfind('A')))