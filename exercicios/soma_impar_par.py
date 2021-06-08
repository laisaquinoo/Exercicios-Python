#Escrever um programa que leia um conjunto de números positivos e exiba se o número 
# lido é par ou ímpar. Exiba ao final a soma total dos números pares lidos e também a 
# soma dos números ímpares lidos. Suporemos que o número de elementos deste conjunto não é 
# conhecido, e que um número negativo será utilizado para sinalizar o fim dos dados.

n= int(input('Digite um nº:'))
par = 0
impar = 0

while n >= 0 :
    if n % 2 == 0:
        par = par + n 

    else:
     impar = impar + n
     #ou impar += n

    n= int(input('Digite um nº:'))

if (par ==0 and impar ==0):
    print('nenhum numero positivo foi digitado')
else:
    print(f'A soma dos numeros pares : {par} / A soma dos numeros impares : {impar}')
 
           