
''''
intNumero = int(input('Informe um numero inteiro:'))
if intNumero % 2 == 0 :
    print(f'{intNumero} é um numero par')
else: print(f'{intNumero} é um numero impar')
'''

'''
base = float(input('informe a base:'))
altura = float(input('informe a altura:'))
if base <= 0:
    print('A base deve ser positiva')
elif altura <= 0:
    print('A altura deve ser positiva')
elif base == altura:
    print('é um quadrado')
else:
    print('é um retangulo')
'''
import sys
a = float(input('Valor de A'))
b = float(input('Valor de B'))
c = float(input('Valor de C'))
if a == 0:
    sys.exit('Não é equação do 2 grau')

delta = b**2 - 4 * a * c
if delta < 0:
    sys.exit('Não existe raíses reais!') 

 # Calcular as raizes  