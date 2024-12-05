'''
   Faça um programa que solicite um valor n inteiro positivo e 
   imprima na tela o seguinte padrão:

   para n = 4

   o programa deverá imprimir

   1
   2 2
   3 3 3
   4 4 4 4
'''

n = int(input('Informe um valor inteiro positivo:'))

for i in range(0, n+1):
    print(f'{i}' * i)

