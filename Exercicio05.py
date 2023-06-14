class Pessoa:
    def __init__(self, nome=None, idade=18, peso=60, altura=1.64):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def mostrar(self):
        print("STATUS:")
        print(f"Seu nome é {self.nome}, sua idade é {self.idade}, seu peso é {self.peso}, sua altura é {self.altura}")

    def envelhecer(self):
        self.idade += 1
        print("ENVELHECENDO...")
        if self.idade < 21:
            self.altura += 0.05

    def engordar(self):
        self.peso += 2
        print("ENGORDANDO...")

    def emagrecer(self):
        self.peso -= 1
        print("PERDENDO PESO...")

    def crescer(self):
        self.altura += 0.05
        print("CRESCENDO! ")

if __name__ == "__main__":
    nome_pessoa = input("Digite seu nome: ")
    idade_pessoa = int(input("Digite a sua idade: "))
    peso_pessoa = int(input("Digite o seu peso: "))
    altura_pessoa = float(input("Digite a sua altura: "))
    pessoa = Pessoa(nome=nome_pessoa, idade=idade_pessoa, peso=peso_pessoa, altura=altura_pessoa)
    while True:
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        pessoa.mostrar()
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        n = input("Escolha entre [ENVELHECER, ENGORDAR, EMGRECER E CRESCER] ").upper()
        if n == 'ENVELHECER':
            pessoa.envelhecer()
        elif n == 'ENGORDAR':
            pessoa.engordar()
        elif n == 'EMAGRECER':
            pessoa.emagrecer()
        elif n == 'CRESCER':
            pessoa.crescer()
        elif n == "STOP":
            break
        else:
            print("[*]")
            print("DIGITE O QUE PEDIMOS!!! E CORRETAMENTE!! ")
            print("[*]")