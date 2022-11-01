import colorama
from colorama import Fore
from colorama import Style
salario = float(input('digite o salario:'))
if salario <= 1250:
    print(Fore.GREEN+f'o novo salário reajustado em 15% será R${salario+(salario*0.15)}')
else:
    print(Fore.GREEN+f'o novo salário reajustado em 10% será R${salario+(salario*0.1)} ')