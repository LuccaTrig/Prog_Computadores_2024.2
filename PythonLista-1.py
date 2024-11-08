'''
Faça um programa que aceita um número de até 4 dígitos (0 a 9999) e exiba a soma dos seus algarismos.
'''

#Dica // e %

numero = int(input('Numero: '))
numMilhar = numero // 1000
restoCent = numero % 1000
baseCent = numMilhar
numCent = baseCent // 100
restoDecim = baseCent % 100
baseDecim = restoDecim
numDecim = restoDecim // 10
restoUnid = baseDecim % 10
Unidade = restoUnid

print(f'Numero: {numero}. Milhar:{numMilhar}; Centena: {numCent}; decimal: {numDecim}; Unidade: {Unidade} ')
