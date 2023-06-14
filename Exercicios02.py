class Quadrado:
    def __init__(self, lado1=0, lado2=0):
        self.lado1 = lado1
        self.lado2 = lado2
    def mudar_valor_lado(self):
        n1 = int(input("mudando os valores "))
      #  n2 = int(input("mudando o valor do lado 2 "))
        self.lado2 = n1
        self.lado1 = n1
    def mostrar_valores(self):
        print(f"lado 1: {self.lado1}")
        print(f"lado 2: {self.lado2}")
    def calcula_area(self):
        calculo = self.lado1 * self.lado2
        print(f"a area do quadro é {calculo}")

if __name__ == "__main__":
    quadrado = Quadrado()
    quadrado.mostrar_valores()
    quadrado.mudar_valor_lado()
    quadrado.mostrar_valores()
    quadrado.calcula_area()