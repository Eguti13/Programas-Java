numeros = [10,4,5,6,8,4,2,9,8,9,5,6]
print(numeros[-1]) #imprime el ultimo elemento de la lista (o numero a escoger)

ordenados = sorted(numeros) #organiza los datos de menor a mayor
print(ordenados)

numeros.append(100) #agrega un dato a la cola
print(numeros)
print(len(numeros)) #len= cantidad de elementos de una lista

numeros.insert(2,240) #agrega numeros a la lista en la posicion escogida antes de la coma
print(numeros)

numeros.pop(5) #se elimina el elemento que se encuentre en la posicion seleccionada
print(numeros)

del numeros [2:4] #los ':' son para eliminar los elementos entre esas dos posiciones
print(numeros)

print(numeros.index(10)) #posicion en la lista en donde se encuentra el numero escogido

numeros_no_repetidos = set(numeros) #filtrar los numeros
print(list(numeros_no_repetidos))

