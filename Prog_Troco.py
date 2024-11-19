'''

Faça um programa que solicite ao usuário um valor decimal positivo (esse valor 
corresponde ao valor de um saque em um terminal de caixa eletrônico) e que calcule a quantidade de 
cédulas de R$ 100,00, R$ 50,00, R$ 20,00, R$ 10,00, R$ 5,00 e R$ 2,00 e de moedas de R$ 1,00, R$ 
0,50, R$ 0,25, R$ 0,10, R$ 0,05 e R$ 0,01.

'''

import sys
valor = float(input('Insira o valor pago para o calculo do troco: '))
if valor < 0:  sys.exit('Não é um valor valido')

troco100 = valor // 100
resto100= valor % 100
troco50 = resto100 // 50
resto50 = resto100 % 50
troco20 = resto50 // 20
resto20 = resto50 % 20
troco10 = resto20 // 10
resto10 = resto20 % 10
troco5 = resto10 // 5
resto5 = resto10 % 5
troco2 = resto5 // 2 
resto2 = resto5 % 2


#Calculo moedas


centavos = valor - int(valor)
moedas50 = centavos // 0.50
restom50 = centavos % 0.50
moedas25 =  restom50 // 0.25
restom25 = restom50 % 0.25
moedas10 = restom25 // 10
restom10 = restom25 % 10
moedas5 = restom10 // 5
moedas1 = restom10 % 5

print(f'O valor sera pago em cedulas de: \n 100 reais:{troco100} \n 50 reais:{troco50} \n 20 reais:{troco20} \n 10 reais:{troco10} \n 5 reais:{troco5} \n 2 reais:{troco2} \n e moedas de: \n 1 real:{moedas1} \n 50 centavos:{moedas50} \n 25 centavos:{moedas25} \n 10 centavos:{moedas10} \n 5 centavos:{moedas5} \n 1 centavo:{moedas1}')
