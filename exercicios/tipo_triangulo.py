print ('===== LADOS DO TRIANGULO =====')
lado1=int(input('INSIRA o TAMANHO DO LADO 1: ') )
lado2=int (input ('INSIRA o TAMANHO DO LADO 2:') )
lado3=int (input ('INSIRA o TAMANHO DO LADO 3:') )

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1+ lado2 :
    if lado1 == lado2 == lado3:
        print ('ESTE É UM TRIANGULO EQUILÁTERO')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3 :
        print ('ESTE É UM TRIANGULO ISÓCELES')
    else:
          print ('ESTE É UM TRIANGULO ESCALENO')   
else:
    print ('NÃO É POSSIVEL FORMAR UM TRIANGULO!')      