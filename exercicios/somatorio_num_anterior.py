#calcule o somatorio de todos os numeros  anteriores até o numero digitado
n=int(input('Digite um nº:'))
soma=0
for i in range (0,n+1):
    soma += i
print (soma)