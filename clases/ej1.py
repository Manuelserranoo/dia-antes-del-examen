class Roma:
    #pasar de numeros enteros a numeros romanos.
    def __init__(self, numero):
        self.numero = numero
        self.romano = ""
        self.valores = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        self.simbolos = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    def convertirnumeros(self):
        for i in range(len(self.valores)):
            while self.numero >= self.valores[i]:
                self.numero -= self.valores[i]
                self.romano += self.simbolos[i]
        return self.romano
        




if __name__ == "__main__":
    numero = int(input("Ingrese un numero: "))
    romano = Roma(numero)
    print(romano.convertirnumeros())