def suma_trampa():
    try:
        operacion = "2"+ 5
    except TypeError:
        print("Error: No se puede sumar un str con un int")
    return 



if __name__ == "__main__":
    suma_trampa()