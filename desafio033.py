n1 = float(input('digite o primeiro número:'))
n2 = float(input('digite o segundo número:'))
n3 = float(input('digite o terceiro número:'))
maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
print(f'o maior é {maior}')
menor = n1
if n2< menor:
    menor = n2
if n3< menor:
    menor = n3
print(f'o menor é {menor}')