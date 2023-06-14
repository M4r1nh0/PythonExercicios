
class Tamagushi:
    def __init__(self, nome=None, fome=0, saude="Saudavel", idade=1, c=0, humor="Bem humorado"):
        self.nome = nome
        self.idade = idade
        self.saude = saude
        self.fome = fome
        self.c = c
        self.humor=humor

    def mostrar(self):
        print("STATUS: ")
        print(f"NOME: {self.nome} | IDADE: {self.idade} | SAUDE: {self.saude} | HUMOR: {self.humor}")

    def alterar_nome(self):
        nome_tamagushi = input("Qual nome vc deseja para o seu tamagushi?: ")
        self.nome = nome_tamagushi
        print("Nome alterado com sucesso!")

    def fome_tamagushi(self):
        self.fome = 0
        print("TAMAGUSHI ALIMENTADADO")

    def alterar_idade(self):
        #idade_tamagushi = int(input("Altera a idade do seu bichinho: "))
        self.idade += 1
        print(f"Idade aumentada! {self.idade}")

    def saude_tamagushi(self):
        cuidado = input("Deseja deixar seu tamagushi saudavel?: [SIM | NÃO] ")
        if cuidado == "sim":
            print("Seu tamagushi está saudavel")
            self.saude = "SAUDAVEL"
            self.c = 0
        elif cuidado == "não" or cuidado == "nao":
            print("Seu tamagushi pode ficar mal")
            self.c += 1
            if self.c == 3 or self.c == 4:
                self.saude = "Quase doente"
                print(f"seu tamagushi está {self.saude} ajude-o antes que piore!")
            elif self.c == 5 or self.c == 6:
                self.saude = "Doente"
                print("[*][*][*][*][*][*][*][*][*][*]")
                print(f"seu tamagushi está {self.saude} cuide dele imediatamente")
                print("[*][*][*][*][*][*][*][*][*][*]")


if __name__ == "__main__":
    n = input("Deseja cuidar de um tamagushi? [SIM | NÃO] ").lower()
    nome_t = input("Digite o nome do seu tamagushi: ")
    #idade_t = int(input("Digite a idade do seu tamagushi "))
    tamagushi = Tamagushi(nome=nome_t)
    while n == 'sim':
        print("[*]=-=-=-=-=-=[*]")
        tamagushi.mostrar()
        print("[*]=-=-=-=-=-=[*]")
        escolha = input("Escolha entre [NOME, IDADE, FOME e SAUDE] ")
        tamagushi.fome += 1
        #print(tamagushi.fome)
        if tamagushi.fome > 2:
            print("SEU TAMAGUSHI ESTÁ COM FOME ALIMENTE-O")
        if tamagushi.fome >= 2 and tamagushi.saude == "Quase doente":
            print("Seu tamagushi está mal humorado!")
            tamagushi.humor = 'mal humorado'
        elif tamagushi.fome >= 2 and tamagushi.saude == "Doente":
            print("Seu tamagushi está PUTO")
            tamagushi.humor = "PUTO!"
        else:
            tamagushi.humor = "bem humorado"
        if escolha == "nome":
            tamagushi.alterar_nome()
        elif escolha == "idade":
            tamagushi.alterar_idade()
        elif escolha == "fome":
            tamagushi.fome_tamagushi()
        elif escolha == "saude":
            tamagushi.saude_tamagushi()