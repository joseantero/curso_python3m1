dis = float(input('digite a distancia da viagem em KM:'))
print('para viagens de até 200km,cobra-se R$0.5 p/ km \npara passagens acima de 200km, cobra-se R$0.45 p/ km \n carregando valor total... ')
if dis<= 200:print(f'o valor total da passagem será R${dis*0.5:.2f}')
else:print(f'a valor total da passagem será R${dis*0.45:.2f}')