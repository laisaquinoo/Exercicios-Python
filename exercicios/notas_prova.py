nome= input ('INSIRA SEU NOME:')
B1=float (input('INSIRA A NOTA DA B1:') )
B2=float (input ('INSIRA A NOTA DA B2:') )

media=(B1+B2)/2

if  media >= 7:
    print (f'PARABÉNS {nome} VOCÊ FOI A PROVADO COM A MEDIA {media}')
else :
    print(f'ATENÇÃO {nome} VOCÊ FICOU DE EXAME.')
    ex=float (input('INSIRA SUA NOTA DO EXAME:')) 
    mf=(ex+media)/2 

if  mf>=5 :
    print(f'PARABÉNS {nome} VOCÊ FOI APROVADO COM A MEDIA FINAL DE {mf} ')
else: 
    print(f'ATENÇÃO !!  {nome} VOCÊ FICOU DE DP!!')