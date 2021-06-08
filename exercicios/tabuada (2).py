#apartir de um numero digitado pelo usuario, exiba a tabuada 
num=int(input('Digite a tabuada do numero que deseja ver:'))
mult =1 
while mult <= 10 :
    print (f'{num}x{mult}= {num*mult}')
    mult = mult + 1