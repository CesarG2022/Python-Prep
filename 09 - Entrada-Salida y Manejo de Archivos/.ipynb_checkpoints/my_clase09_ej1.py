import sys  

if(len(sys.argv)==4):
    for c, i in enumerate(sys.argv):
        if c>0:
            print("el parametro", c, "es:" , i)
else:
    print("ERROR: la cantidad de argumentos debe ser 3")
    print("Ejemplo: julio cesar 1990")

