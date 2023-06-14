class Bola:
    def __init__(self, cor='Branco', circunferencia=4, material="Borracha"):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
    def mostrar_cor(self):
        print(self.cor)
    def mudar_cor(self):
        n = input("Escolha uma cor entre [Branco, Preto, vermelho e azul] ").upper()
        if n == "BRANCO" or n == "PRETO":
            #print(f"a cor é igual a {n}")
            self.cor = n
        elif n == "VERMELHO" or n == "AZUL":
           # print(f"a cor é igual a {n}")
            self.cor = n

if __name__ == "__main__":
    bola = Bola()
    while True:
        escolha = input("Escolha entre, [MOSTRAR, MUDAR e STOP]  ")
        if escolha == "mostrar":
            bola.mostrar_cor()
        elif escolha == "mudar":
            bola.mudar_cor()
        elif escolha == "stop":
            break
