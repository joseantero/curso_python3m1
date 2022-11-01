import random
from time import sleep
numero = int(random.uniform(0,5))
print('carregando jogo....')
n1= int(input('digite o número a ser sorteado de 0 á 5:'))
sleep(2)
print(f'_*_'*20)
print('processando.........')
print(f'_*_'*20)
if numero == n1:
    print(f'Parabéns você acertou o número sorteado é {n1}')
else:
    print(f'Você perdeu, o número sorteado foi: {numero:.1f}')


