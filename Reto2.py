distancia_camarasm, velocidad_kmH, tiempo_segundos = input().split( )

distancia_camarasm = float(distancia_camarasm)
velocidad_kmH = float(velocidad_kmH)
tiempo_segundos = float(tiempo_segundos)

tiempo_horas=float(tiempo_segundos/3600)
distancia_camaraskm=float(distancia_camarasm/1000)
velocidad_media = round((distancia_camaraskm/tiempo_horas),1)

porcentaje1= velocidad_kmH*0.2
porcentaje2= velocidad_kmH*0.21
velocidad_kmH1 = velocidad_kmH + porcentaje1
velocidad_kmH2 = velocidad_kmH + porcentaje2

if distancia_camarasm <0 or velocidad_kmH <0 or tiempo_segundos<0:
    print('ERROR')
elif velocidad_media <=  velocidad_kmH:
    print(velocidad_media, 'VELOCIDAD NORMAL')
elif velocidad_media == velocidad_kmH or velocidad_media < velocidad_kmH1:
    print(velocidad_media, 'NUEVO RECORD')
elif velocidad_media >= velocidad_kmH1 or velocidad_media > velocidad_kmH2:
    print(velocidad_media, 'ENTREVISTA')