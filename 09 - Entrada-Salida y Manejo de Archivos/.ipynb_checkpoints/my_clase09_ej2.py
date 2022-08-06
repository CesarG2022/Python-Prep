import sys
import os
import datetime

if len(sys.argv)==1:
    marca_tiempo=datetime.datetime.now()
    marca_tiempo=str(datetime.datetime.timestamp(marca_tiempo))
    lluvia=input('introduzca True si llovio o False en caso contrario')
    temperatura=input('introduzca temperatura en grados celsius')
    humedad=input('introduzca humedad en porcentaje')

    linea= marca_tiempo + "," + temperatura + "," + humedad + "," + lluvia

    nuevo_dato= open('my_clase09_ej2.csv','a')
    nuevo_dato.write(linea+'\n')
    nuevo_dato.close()
else:
    print('ERROR: para usar el script no debe ingresar argumentos')