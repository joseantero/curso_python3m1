n1 = int(input('digite um numero de 0 á 9999:'))
und = n1 // 1 % 10
dez = n1 // 10 % 10
cent = n1 // 100 % 10
milh = n1 // 1000 % 10
#acrescentar = n1.replace(""," ").split()
#und = acrescentar[3]
#dez = acrescentar[2]
#cent = acrescentar[1]
#milh = acrescentar[0]
print(f'unidade é {und} ; \n dezena é {dez} ; \n centena {cent} ; \n milhar é {milh} ')