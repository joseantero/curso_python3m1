import colorama
from colorama import Fore
from colorama import Style
colorama.init()
n1 = int(input(Fore.WHITE+Style.NORMAL+'digite um número:'))
if n1 % 2 == 0:
    print(Fore.GREEN+Style.NORMAL+f' o número digitado {n1} é par')
else:
    print(Fore.RED+Style.BRIGHT+f'o numero digitado {n1} é impar')