nome=input('INSIRA SEU NOME: ') 
sexo=input('DIGITE [1]MASCULINO OU [2] FEMININO: ') 
altura=float(input ('INSIRA SUA ALTURA:') )

if sexo == "1":
    H= (72.7*altura) - 58
    print (f'{nome} SEU PESO IDEAL É %.1f '%H)

elif sexo == "2":
    F= (62.1 *altura) - 44.7
    print (f'{nome} SEU PESO IDEAL É %.1f' %F)

if  altura < 0.5  and altura > 2.2:
    print ('ATENÇÃO, ERRO NA SUA ALTURA!')
