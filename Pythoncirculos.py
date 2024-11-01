'''
Faça um programa que solicite ao usuário o raio de uma circinferência
e calcule a área di círculo eo comprimento da curcunferência
'''

Raio          = float(input('Raio da circunferencia ='))

#calculos

AreaDoCirc    = Raio**2 * 3.14
CompCirc      = 2 * 3.14 * Raio 

print(f'A circunferencia de Raio = {Raio} tem a Área ={AreaDoCirc} e comprimento de circunferencia ={CompCirc}')