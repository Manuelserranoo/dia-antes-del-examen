def onperacion():
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    try:
        operacion = num1/num2
    except ZeroDivisionError:
        print("No se puede dividir por 0")
    return operacion




if __name__ == "__main__":
    print(onperacion())