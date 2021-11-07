def mutiplicar(a,b):
     print("Estas ejecutando la mutiplicacion")
     c = a*b
     return c

def comparNumeros (num1: int,num2: int) -> str:
    if type(num1) is not int or type(num2) is not int:
        raise Exception("no son 2 enteros")
    if num1 > num2:
        print ("El primer valor es mayor")
    elif num1 < num2:
        print("El segundo valor es mayor")
    else:
        print ("Son iguales")

variable_global = 10

if __name__ ==  '_main_':
     var1 = 2
     var2 = 3
     resultado = mutiplicar(var1, var2)
     variable_global += 1
     print (variable_global)
     comparNumeros (8, 5)