def esprimo(numero=1):
    '''
    Determina si numero es primo o no
    '''

    for n in range(2,(numero//2)+1):
        if (numero%n==0):
            return False
    return True

#-----------------------------------------------------------------------------------------------

def solo_primos(lisloc):
    soloprimos=[]
    for c in lisloc: 
        if (esprimo(c)):
            soloprimos.append(c)
    return soloprimos

#-----------------------------------------------------------------------------------------------

def repetido(lisloc, extremo):
  
    lis_repet=[]
    
    for x, i in enumerate(lisloc):
        lis_repet.append(lisloc.count(i))
    if extremo=="max":
        max_repet=max(lis_repet)
        pos_max=lis_repet.index(max_repet)
        print( lisloc[pos_max],"aparece", max_repet,"veces")
    elif extremo=="min":
        min_repet=min(lis_repet)
        pos_min=lis_repet.index(min_repet)
        print( lisloc[pos_min],"aparece", min_repet,"veces")
    else:
        print("la opcion ingresada no es valida, vuelva a intentarlo")

    
#-----------------------------------------------------------------------------------------------

def conver_temp(valor,origen, destino):
    Resultado=float
    if(origen=="C"):
        if(destino=="F"):
            Resultado= (valor * 9/5 ) + 32
        elif(destino=="K"):
            Resultado= valor + 273.15
        else:
            print("parametro destino incorrecto, vuelva a intentarlo")
    elif (origen=="F"):
        if(destino=="C"):
            Resultado= (valor - 32 ) * 5/9
        elif(destino=="K"):
            Resultado= ((valor - 32 ) * 5/9) + 273.15
        else:
            print("parametro destino incorrecto, vuelva a intentarlo")
    elif (origen=="K"):
        if(destino=="F"):
            Resultado= ((valor-273.15) * 9/5 ) + 32
        elif(destino=="C"):
            Resultado= valor - 273.15
        else:
            print("parametro destino incorrecto, vuelva a intentarlo")
    else:
        print("parametro origen, vuelva a intentarlo")    

    return Resultado

#-----------------------------------------------------------------------------------------------

def factorial(num):
    if num==1:
        return num
    elif(type(num)==int and num>1):
        num = num * factorial(num-1)
        return num
    else:
        print("el numero ingresado debe ser entero y positivo")
   