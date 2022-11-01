import random
from random import shuffle
n1 = input('digite o nome do primeiro aluno:')
n2 = input('digite o segundo:')
n3 = input('digite o terceiro:')
n4 = input ('digite o quarto aluno:')
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print(f'a ordem de apresentação do trabalho é:{lista}')