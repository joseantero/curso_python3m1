frase = str(input('digite uma frase:')).upper().strip()
letraa = frase.count('A')
A1 = frase.find('A')
print(f'a letra A aparece {letraa} vezes; \n a primeira vez na posição: {A1+1} ; \n a ultima vez na posição: {frase.rfind("A")+1}')