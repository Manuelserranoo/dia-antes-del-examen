#realizame un funcion que realice potencias de ecuaciones con 1 variable
def potencia():
    try:
        x = int(input("Ingrese el valor de x: "))
        y = int(input("Ingrese el valor de y: "))
        potencia = x**y
    except ValueError:
        print("Error: No se puede elevar un str a un int")
    
    return potencia



if __name__ == "__main__":
    print(potencia())

