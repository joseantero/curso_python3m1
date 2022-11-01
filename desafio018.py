import math
angulo = float(input('insira o angulo em graus para receber os valores de seno/cos/tan:'))
x = 0.0174533 * angulo
print(f'você inseriu o angulo de: {x}rad ou {angulo}° , sendo assim seu seno é de:{math.sin(x):.3f}'
      f'\n cosseno: {math.cos(x):.3f} e sua tangente:{math.tan(x):.3f}')