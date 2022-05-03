#un invidivuo desea invertir su capital en un banco y quieres saber cuanto dinero ganara despues de un mes si el banco paga a razon de 15% anual

INTERES_ANUAL=0.15
INTERES_MENSUAL=INTERES_ANUAL /12


capital=float(input( 'ingrese el capital a invertir'))
rendimiento= capital*INTERES_MENSUAL

print(f'su rendimiento despues de un mes es: {rendimiento:.2f}')

PORCENTAJE_COMISION = 0.1
salario_base = float(input('ingrese sueldo base: '))
comisiones = salario_base*PORCENTAJE_COMISION
salario_total = salario_base + comisiones

print(f'sus comisiones este mes son: {comisiones}')
print(f'Su salario total este mes es de: {salario_total}')


"""una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto debera pagar finalmente por su compra"""

DESCUENTO = 0.15

total_compra = float(input('ingrese el total de la compra'))
descuento_compra = total_compra * DESCUENTO
total = total_compra - descuento_compra

print(f'el valor total a pagar es: {total}')


#Un alumno desea saber cual sera su calificacion final en la materia de Algoritmos. Dicha calificacion se compone de los siguientes porcentajes: 40% promedio ded sus tres calificaciones parciales, 50% de la calificacion de examen finaal y 10% de la calificacion del trabajo final

PORCENTAJE_CALIFICACIONES = 0.4
PORCENTAJE_EXAMEN = 0.5
PORCENTAJE_TRABAJO = 0.1

calificacion1, calificacion2, calificacion3 = input('ingrese las 3 calificaciones parciales separadas por espacios').split()

nota_calificaciones = (float(calificacion1) + float(calificacion2) + float(calificacion3)/3)* PORCENTAJE_CALIFICACIONES
nota_examen_final = float(nota_examen_final) * PORCENTAJE_EXAMEN

