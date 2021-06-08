N1=int(input('INSIRA UM NUMERO: ') )
N2=int(input ('INSIRA O SEGUNDO NUMERO:') )

print ('''[1]– Adição
[2] – Subtração
[3] – Multiplicação
[4] – Divisão''')
opcao=int(input('INSIRA A OPERAÇÃO DESEJADA: ') )

if opcao == 1 :
    resultado=N1+N2
    print (f'O RESULTADO É {resultado}')
    
elif opcao == 2 :
    resultado=N1-N2
    print (f'O RESULTADO É {resultado}')

elif opcao == 3 :
    resultado=N1*N2
    print (f'O RESULTADO É {resultado}')
    
elif opcao == 4 :
    resultado=N1/N2
    print (f'O RESULTADO É {resultado}')

else :
    print ('ESTA OPÇÃO NÃO É POSSIVEL')

