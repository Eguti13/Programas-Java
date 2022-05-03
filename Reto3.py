
numero_registros = int(input())
lista1=edad, hemoglobina_glicosilada, obesidad_limite, tensistolica, tendiastolica= input().split()

for registro in range(numero_registros):
    lista1.append(lista1)

edad=int(edad)
hemoglobina_glicosilada= int(hemoglobina_glicosilada)
obesidad_limite= int(obesidad_limite)
tensistolica=int(tensistolica)
tendiastolica=int(tendiastolica)

edad_vulnerable = edad >= 80

if edad >= 80:
    print(edad_vulnerable)
else:
    print('NO DISPONIBLE')
if hemoglobina_glicosilada > 7:
    print(edad_vulnerable)
else:
    print('NO DISPONIBLE')
if obesidad_limite >= 30:
    print(edad_vulnerable)
else:
    print('NO DISPONIBLE')
if tensistolica >= 140:
    print(edad_vulnerable)
else:
    print('NO DISPONIBLE')
if tendiastolica <90:
    print(edad_vulnerable)
else:
    print('NO DISPONIBLE')