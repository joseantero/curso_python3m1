import datetime
from datetime import date
bi = int(input('digite o ano a ser verificado ou digite 0 para verificar o ano atual:'))
if bi == 0:
    bi = date.today().year
if bi % 4 == 0 and (bi % 100) > 0 or bi % 4 == 0 and bi % 400 == 0 and bi % 100 == 0:
    print(f'o ano {bi} é bissexto')
#if bi % 4 == 0 and bi % 400 == 0 and bi % 100 == 0:
   # print(f'O ano  {bi} é bissexto')
else:
    print(f'o ano {bi} não é bissexto')