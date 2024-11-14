''' Uma família fez uma viagem de carro e quer detalhes sobre o desempenho do veículo. 
Faça um programa que pergunta: o momento inicial da partida (hora e minuto), o momento de chegada 
(hora e minuto), o número de segundos parados para descanso, o número de litros de combustível gasto 
(em l), o preço do litro de combustível (em R$) e a distância percorrida (em Km); 
Após receber os dados, o programa informa dados típicos de um computador de bordo: 
a) o tempo de viagem (em segundos)
b) a velocidade média (Km/h) global e a velocidade média em movimento (Km/h)
c) o custo da viagem com combustível (em R$)
d) o desempenho do carro (em Km/l, l/h e R$/Km) '''

import sys

inicioViagem =  int(input('formato ex: 22:11 = 2211. Informe o horario de inicio da viagem:'))
if inicioViagem > 2359:sys.exit('Horario invalido!')
horaTeste = inicioViagem % 100
if horaTeste > 60:sys.exit('horaio invalido!')


print(f'inicio: {inicioViagem}. Hora teste: {horaTeste}')