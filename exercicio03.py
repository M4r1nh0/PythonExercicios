class Retangulo:
    def __init__(self, altura=0, largura=0):
        self.altura = altura
        self.largura = largura
    def mudar_valor_dados(self):
        n1 = int(input("mudar valor altura "))
        n2 = int(input("mudar valor largura "))
        self.altura = n1
        self.largura = n2
    def mostrar_valores(self):
        print(f"altura {self.altura}")
        print(f"largura {self.largura}")
    def calcular_area(self):
        calculo_area = self.altura * self.largura
        print(f"A area do retangulo é {calculo_area}")
    def calcular_perimetro(self):
        calculo_perimetro = (self.altura*2)+(self.largura*2)
        print(f"O perimetro do retangulo é {calculo_perimetro}")

if __name__ == "__main__":
    retangulo = Retangulo()
    retangulo.mostrar_valores()
    retangulo.mudar_valor_dados()
    retangulo.mostrar_valores()
    retangulo.calcular_perimetro()
    retangulo.calcular_area()