km = float(input('digite a quantidade de quilometros rodados por você:'))
dias = int(input('digite por quantos dias você alugou o carro:'))
print(f'O carro ficou alugado por {dias} dias , com quilometragem de {km}km, portanto '
      f'\n 'f'você deverá pagar R${km*0.15+dias*60:.2f} ')