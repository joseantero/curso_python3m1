import random
from random import choice
x = input('digite o nome do primeiro aluno a ser sorteado para apagar o quadro:')
y = input('digite o segundo:')
z = input('digite outro:')
t = input('digite o último:')
names = [x,y,z,t]
print(f'o aluno sorteado para apagar o quadro é :{random.choice(names)}')