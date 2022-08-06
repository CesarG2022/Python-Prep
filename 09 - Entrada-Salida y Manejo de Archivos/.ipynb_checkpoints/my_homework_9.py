montañas = {'nombre':[  'Everest','K2','Kanchenjunga','Lhotse','Makalu',
                        'Cho Oyu','Dhaulagiri','Manaslu','Nanga Parbat','Annapurna I'],
            'orden':[1,2,3,4,5,6,7,8,9,10],
            'cordillera':['Himalaya','Karakórum','Himalaya','Himalaya','Himalaya'
                        ,'Himalaya','Himalaya','Himalaya','Karakórum','Himalaya'],
            'pais': ['Nepal','Pakistán','Nepal','Nepal','Nepal','Nepal','Nepal','Nepal',
                    'Pakistán','Nepal'],
            'altura':[8849,8611,8586,8516,8485,8188,8167,8163,8125,8091]}

import sys
import os

encabezado= montañas.keys()
encabezado=",".join(encabezado)

crear_tabla = open('my_clase09_ej3.csv','w')
crear_tabla.write(encabezado+'\n')
for j in range(len(montañas['nombre'])):
    linea=[]
    for i in montañas:
        if type(montañas[i][j])!=str:
            montañas[i][j]=str(montañas[i][j])
        linea.append(montañas[i][j])
   
    linea=",".join(linea)
    crear_tabla.write(linea+'\n')

crear_tabla.close()

print("el tamaño del archivo my_clase09_ej3.csv es:", os.path.getsize('my_clase09_ej3.csv')/1024 ,"MB")

#os.makedirs('clase09_montañas_altas')

os.system('copy my_clase09_ej3.csv clase09_montañas_altas')

print(os.listdir('./clase09_montañas_altas'))