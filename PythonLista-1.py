'''
Faça um programa que aceita um número de até 4 dígitos (0 a 9999) e exiba a soma dos seus algarismos.
'''

numero = int(input('Numero: '))

if: numero < -999

milhar = numero // 1000
numeroCent = numero % 1000
centena = numeroCent // 100
opDecimal = numeroCent % 100
dezena = opDecimal // 10
unidade = opDecimal % 10 
somaAlgarismos = milhar + centena + dezena + unidade

print(f' Numero = {numero} milhar = {milhar} centena = {centena} Dezena = {dezena} unidade = {unidade} soma dos algarismos = {somaAlgarismos}')
