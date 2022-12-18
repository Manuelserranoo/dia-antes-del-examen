def evaluar_lista():
    paises = { 'españa':'español', 'eeuu':'inglés', 'italia':'italiano' } 
    try:
        paises['españa']
    except KeyError:
        print("Error: La clave del diccionario no se encuentra, debes probar con otra que sí exista.")
    return paises


if __name__ == "__main__":
    print(evaluar_lista())