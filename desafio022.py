nome = input(str('Digite o nome completo:'))
separado = nome.strip().split()
letras = separado[0]
remover = nome.replace(" ","")
print(f'Nome digitado maiúsculo:{nome.upper()}')
print(f'Nome em minúsculo:{nome.lower()}')
print(f'quantidade de caracteres={len(nome)}')
print(f'quantidade de caracteres sem espaços :{len(remover)}')
print(f'primeiro nome é {letras} e tem {len(letras)} letras')
