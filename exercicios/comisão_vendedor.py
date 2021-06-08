nome_vendedor=(input('Digite o nome do vendendor:'))
codigo_peca=int(input('Digite o codigo da peça:'))
valor=float(input('Digite o valor da peça:'))
quantidade=int (input('Digite a quantidade vendida:'))
resultado=valor*quantidade*0.05
print('A comisão do {} é {:.2f}'.format(nome_vendedor,resultado))