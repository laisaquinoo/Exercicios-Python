nome=(input('Insira seu nome:'))
nota1=float(input('Insira sua primeira nota:'))
nota2=float(input('Insira sua segunda nota:'))
R=(nota1+nota2)/2
if R>=7:
    print( nome ,'sua media foi ', R ,  ' // ALUNO APROVADO!')
else:
    print( nome, 'sua media foi ', R, ' // ALUNO REPROVADO!')