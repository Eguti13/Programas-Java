
def total_inventario(tienda):
    valor=0 
    for i in tienda:
        valor+=tienda[i][1]*tienda[i][2]
    return valor

def prom_precios(tienda):
    prom=0 
    for i in tienda:
        prom+=tienda[i][1]
    prom/=len(tienda)
    return prom

def nombre_mayor(tienda):
    x=list(tienda.keys())
    m=tienda[x[0]][1]
    nombre=tienda[x[0]][0]
    for i in tienda: 
        if tienda[i][1]>m:
            m=tienda[i][1]
        nombre=tienda[i][0]
    return nombre

def nombre_menor(tienda):
    x=list(tienda.keys()) 
    m=tienda[x[0]][1]
    nombre=tienda[x[0]][0]
    for i in tienda: 
        if tienda[i][1]<m:
            m=tienda[i][1]
        nombre=tienda[i][0]
    return nombre

def borrar_producto(tienda,producto):
    if producto[0] in tienda:
        tienda.pop(producto[0])
        print(nombre_mayor(tienda),nombre_menor(tienda),round(prom_precios(tienda),1),round(total_inventario(tienda),1)) 
    else:
        print('ERROR')

def actualizar_producto(tienda,producto): 
    if producto[0] in tienda:
        tienda[producto[0]]=producto[1:4]
        print(nombre_mayor(tienda),nombre_menor(tienda),round(prom_precios(tienda),1),round(total_inventario(tienda),1))  
    else:
        print('ERROR') 

def agregar_producto(tienda,producto): 
    if producto[0] in tienda:
        print('ERROR')  
    else:
        tienda[producto[0]]=producto[1:4]
        print(nombre_mayor(tienda),nombre_menor(tienda),round(prom_precios(tienda),1),round(total_inventario(tienda),1)) 

def principal():   
    tienda={1: ["Manzanas", 5000.0, 25],
        2: ["Limones", 2300.0,15],
        3: ["Peras", 2700.0, 33],
        4: ["Arandanos", 9300.0,5],
        5: ["Tomates", 2100.0, 42],
        6: ["Fresas", 4100.0, 3],
        7: ["Helado", 4500.0, 41],
        8: ["Galletas", 500.0, 8],
        9: ["Chocolates",3500.0, 80],
        10: ["Jamon", 15000.0, 10],}

operacion=input()
producto=input().split()
producto[0]=int(producto[0])
producto[2]=float(producto[2])
producto[3]=int(producto[3])
if operacion=='AGREGAR':
    agregar_producto(tienda,producto)
elif operacion=='ACTUALIZAR':
    actualizar_producto(tienda,producto)
elif operacion=='BORRAR':
    borrar_producto(tienda,producto)
