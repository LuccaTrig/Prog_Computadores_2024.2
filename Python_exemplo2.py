'''
   Fazer um programa que fique lendo números inteiros solicitados ao usuário.

   Quando o usuário digitar 0, o programa deve finalizar e imprimir a soma de 
   todos os números digitados bem como a média aritmética.

   O valor 0 não deve entrar na média.
'''


soma = 0
contador = 0

while True:
    numero = int(input("Digite um número inteiro (ou 0 para sair): "))
    
    if numero == 0:
        break  
    
    soma += numero 
    contador += 1 

if contador > 0:
    media = soma / contador  
    print(f"Soma dos números: {soma}")
    print(f"Média dos números: {media:.2f}")  
else:
    print("Nenhum número foi digitado.")