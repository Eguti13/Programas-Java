#Condicionales dobles
edad = int(input('por favor, ingrese su edad:'))

if edad >= 18:
    print('Bienvenido, puede ingresar')
else:
    tiempo_restante = 18 - edad
    print('Por el momento no puede ingresar, intentelo en', tiempo_restante,'años')
print('Gracias por usar nuestro programa')


#Condicionales Anidados
comida_favorita = 'hotdog'
if comida_favorita == 'hotdog':
    print('Te gusta el hotdog')
elif comida_favorita == 'pizza':
    print('Te gusta la pizza')
elif comida_favorita == 'Hamburguesa':
    print('Te gusta la hamburguesa')
else:
    print('Otra comida')


if comida_favorita == 'hotdog':
    print('Te gusta el hotdog')
else:
    if comida_favorita == 'pizza':
        print('Te gusta la pizza')
    elif comida_favorita == 'Hamburguesa':
        print('Te gusta la hamburguesa')
    else:
        print('Otra comida')

