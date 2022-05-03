numero = 1
print('Aprendiendo a usar el while en Python')

while(numero <= 10):
    print(numero)
    numero += 1

print('finalice el while')

#While sumatoria

numero = 10
contador = 1
suma = 0

while(contador<= numero):
    suma = suma + contador
    contador += 1

print(suma)

#while numeros

numero = int(input('ingrese un numero menor a 10'))

while(numero >= 10):
    numero = int(input('Error -> Por favor ingrese un numero menor a 10'))

print('El numero', numero, 'ingresado correctamente')


#While numeros en rango
numero = int(input('ingrese un numero menor a 20 y mayor a 0'))

while numero >= 20 or numero <= 0:
    numero = int(input('ERROR - Por favor, ingrese un numero menor a 20 y mayor a 0'))

print(f'El numero {numero} ha sido ingresado correctamente')


