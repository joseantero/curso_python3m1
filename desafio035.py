import colorama
from colorama import Fore
from colorama import Style
r1 = float(input('digite o valor inteiro da primeira reta:'))
r2 = float(input('digite o valor inteiro da segunda reta:'))
r3 = float(input('digite o valor inteiro da terceira reta:'))
if r1 < r2+r3 and r2 < r1 + r3 and r3 < r1 +r2:
    print(Fore.GREEN+Style.BRIGHT+'as três retas podem formar um triângulo')
else:
    print(Fore.RED+Style.BRIGHT+'com as três retas NÃO É possivel forma um triângulo')

