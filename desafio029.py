import colorama
from colorama import Fore
from colorama import Style
velocidade = float(input('digite a velocidade do carro em KM/H:'))
colorama.init
if  80>=velocidade:

    print(Fore.RED+Style.BRIGHT+'Uma otima viagem , siga abaixo de 80km/h para evitar multas')
else:
    print(Fore.RED+Style.BRIGHT+f'VOCÊ FOI MULTADO!!\nA multa vai custar R$7,00 a cada km ultrapassado \nvoce foi multado em R${(velocidade - 80)*7:.2f}')
