def precio_mayor(inventario):
    x=list(inventario.keys()) 
    y=inventario[x[0]][1]
    nombre=inventario[x[0]][0]
    for i in inventario:
        if inventario[i][1]>y:
            y=inventario[i][1]
            nombre=inventario[i][0]
    return nombre

def precio_menor(inventario):
    x=list(inventario.keys()) 
    y=inventario[x[0]][1]
    nombre=inventario[x[0]][0]
    for i in inventario:
        if inventario[i][1]<y:
            y=inventario[i][1]
            nombre=inventario[i][0]
    return nombre

def promedio_inventario(inventario):
    promedio = 0
    for i in inventario:
        promedio+=inventario[i][1]
    promedio/=len(inventario)
    return promedio

def total_inventario(inventario):
    valor = 0
    for i in inventario:
        valor+=inventario[i][1]*inventario[i][2]
    return valor

def agregar_producto(inventario,producto):
    if producto[0] in inventario:
        print('ERROR')
    else:
        inventario[producto[0]]=producto[1:4]
        print(precio_mayor(inventario),precio_menor(inventario),round(promedio_inventario(inventario),1),round(total_inventario(inventario),1))

def actualizar_producto(inventario,producto):
    if producto[0]in inventario:
        inventario[producto[0]]=producto[1:4]
        print(precio_mayor(inventario),precio_menor(inventario),round(promedio_inventario(inventario),1),round(total_inventario(inventario),1))
    else:
        print('ERROR')

def borrar_producto(inventario,producto):
    if producto[0] in inventario:
        inventario.pop(producto[0])
        print(precio_mayor(inventario),precio_menor(inventario),round(promedio_inventario(inventario),1),round(total_inventario(inventario),1))
    else:
        print('ERROR')


def tienda():
    inventario={   
        1: ["Manzanas", 5000.0, 25],
        2: ["Limones", 2300.0,15],
        3: ["Peras", 2700.0, 33],
        4: ["Arandanos", 9300.0,5],
        5: ["Tomates", 2100.0, 42],
        6: ["Fresas", 4100.0, 3],
        7: ["Helado", 4500.0, 41],
        8: ["Galletas", 500.0, 8],
        9: ["Chocolates",3500.0, 80],
        10: ["Jamon", 15000.0, 10],}

    solicitud=input()
    producto=input().split()
    producto[0]=int(producto[0])
    producto[2]=float(producto[2])
    producto[3]=int(producto[3])
    if solicitud=='AGREGAR':
        agregar_producto(inventario,producto)
    elif solicitud=='ACTUALIZAR':
        actualizar_producto(inventario,producto)
    elif solicitud=='BORRAR':
        borrar_producto(inventario,producto)


tienda()