
#1) Faça um programa que o usuario informe uma temperatura em celcius e exiba essa mesma temperatura convertida em fahrenheit.

print('Para converter um valor em Graus celcius para fahrenheit informe o valor em:')
Celcius = float(input('Celcius ='))
Fahrenheit = Celcius * 1.8 + 32

print(f'1) A temperatura = {Celcius} em graus celcius é equivalente a {Fahrenheit} fahrenheit')


#2) Faça um programa que solicite ao usuario sua altura e seu peso. e que calcule e exiba seu IMC

print('Para o calculo de seu IMC informe:')
Altura = float(input('Altura ='))
Peso = float(input('Peso ='))
IMC = (Peso) / Altura**2
print(f'2) O resultado do seu IMC é = {IMC}')

#3) Faça um programa que soliciete o preço de um produto e um valor percentual de desconto, e que calcule e exiba o preço do produto com desconto

print('Para calcular o desconto de um produto informe:')
preço  = float(input('Preço = '))
desconto = int(input('Desconto ='))
DescontoDecimal = (desconto/100) * preço
PreçoFinal = preço - DescontoDecimal

print(f'3) O preço do produco com desconto é de {PreçoFinal}')

#4)Faça um programa que solicite o salário base de um funcionário, o valor total das vendas e o percentual relativo a comissão. e exiba o valor do salario com a comissão

print('Para o calculo do salario com a comissão informe:')
Salario = float(input('Salario ='))
TotalVendas = float(input('Total de vendas ='))
Comissao = int(input('porcentagem da comissão ='))
comissaoDecimal= (Comissao)/100 * TotalVendas
SalarioFinal = Salario + comissaoDecimal

print(f'4) O salario com a comissão é de {SalarioFinal}')