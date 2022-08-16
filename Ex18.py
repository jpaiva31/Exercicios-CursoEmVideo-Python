import math
n = float(input('Digite o ângulo que você deseja: '))
print('O angulo {} tem o SENO de {}\nO angulo {} tem o Cosseno de {}\nO angulo {} tem a TANGENTE de {}\n'.format(n,math.sin(math.radians(n)),n,math.cos(math.radians(n)),n,math.tan(math.radians(n))))
