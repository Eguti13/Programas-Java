salario, hora_extra, bonificacion = input().split() 

salario = float(salario)
hora_trabajo = float(salario/190)
hora_extra = float(hora_extra)
adicional_bono = float(bonificacion)
adicional_extra = float(hora_trabajo*34)/100 * float(hora_extra)
total_bono = float(salario * 6.1)/100 * float(bonificacion)
total_extras = float(adicional_extra) + float(hora_trabajo) * float(hora_extra)

aporte_salud = (salario*0.01) + (total_bono*0.01) + (total_extras*0.01)
aporte_pension = (salario*0.01) + (total_bono*0.01) + (total_extras*0.01)
aporte_caja = (salario*0.01) + (total_bono*0.01) + (total_extras*0.01)
total_descuentos = aporte_salud + aporte_pension + aporte_caja

salario_con_recargos = round(salario + total_extras + total_bono, 1)
salario_con_descuentos = round(salario + total_extras + total_bono - total_descuentos, 1)

print(salario_con_recargos, salario_con_descuentos)