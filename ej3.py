def paises():
    paises = {"españa", "francia", "italia", "alemania", "portugal"}
    try:
       paises["españa"]
    except TypeError:
        print("El pais no existe")

    return paises




if __name__ == "__main__":
    print(paises())