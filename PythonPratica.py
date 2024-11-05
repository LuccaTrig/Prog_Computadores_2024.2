print('Para o calculo de seu IMC informe:')
Altura = float(input('Altura ='))
Peso = float(input('Peso ='))
IMC = (Peso) / Altura**2
print(f'2) O resultado do seu IMC é = {IMC}')

if IMC < 17:
    print('Abaixo do peso')
elif IMC < 25:
       print('Peso normal')
elif IMC < 30:
         print('Sobre peso')
elif IMC < 35:
          print('Obesidade I')
elif IMC < 40: 
           print('Obesidade II')

else: print('Obesidade III')