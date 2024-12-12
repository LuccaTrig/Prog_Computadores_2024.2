
#Exercicio 4

palavra = input('Insira uma palavra:')

palavra_inv = ''

for i in range (len(palavra)-1, -1, -1):
    palavra_inv += palavra[i]

if palavra == palavra_inv:
    print('A palavra é um palindromo')
