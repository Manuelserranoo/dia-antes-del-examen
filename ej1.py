def onperacion():
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    try:
        operacion = num1/num2
    except ZeroDivisionError:
        print("No se puede dividir por 0")
    return operacion

def evaluar_lista():
    lista = [1,2,3,4,5,6,7,8,9,10]
    print(lista[14])
    


if __name__ == "__main__":
    print(evaluar_lista())