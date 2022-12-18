#crear una matriz de tamaño especificado por el usuario, llenarla de números aleatorios y mostrarla en pantalla.
palabra = "defend the east wall"
a =  palabra.replace(" ","")
def crear_matriz(m,n):
    for j in range(n):
        return [[0 for j in range(n)] for i in range(m)]
    for k in j:
        if k == a[0]:
            matriz.append(k)

filas = int(input("Ingrese la clave: "))
columnas  = len(a)
if __name__ == "__main__":
    matriz = crear_matriz(filas,columnas)
    print(matriz)