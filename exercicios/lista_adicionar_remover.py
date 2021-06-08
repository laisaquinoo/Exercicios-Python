frutas=['maça','morango','melancia','mamão']
print(frutas)
remover=input('Qual fruta você gostaria de remover?')
frutas.remove(remover)
adicionar=input('Qual fruta você deseja acrescentar?')
frutas.append(adicionar)
print('Nova lista', frutas)
