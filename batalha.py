import random

class Pokemon:
    def __init__(self, nome, tipo, vida, ataque):
        self.nome = nome
        self.tipo = tipo
        self.vida = vida
        self.ataque = ataque

    def atacar(self, alvo):
        alvo.vida -= self.ataque

        if alvo.vida < 0:
            alvo.vida = 0

        print(f"\n{self.nome} atacou {alvo.nome}!")
        print(f"{alvo.nome} perdeu {self.ataque} de vida.")
        print(f"Vida restante de {alvo.nome}: {alvo.vida}")

pikachu = Pokemon("Pikachu", "Elétrico", 100, 25)
charmander = Pokemon("Charmander", "Fogo", 110, 20)
squirtle = Pokemon("Squirtle", "Água", 120, 18)

print("=== ESCOLHA SEU POKÉMON ===")
print("1 - Pikachu")
print("2 - Charmander")
print("3 - Squirtle")

opcao = int(input("Digite sua opção: "))

if opcao == 1:
    jogador = pikachu
elif opcao == 2:
    jogador = charmander
elif opcao == 3:
    jogador = squirtle
else:
    print("Opção inválida!")
    jogador = None

if jogador is not None:
    adversarios = [p for p in [pikachu, charmander, squirtle] if p != jogador]
    adversario = random.choice(adversarios)

    print(f"\nVocê escolheu {jogador.nome}!")
    print(f"Seu adversário é {adversario.nome}!")

    turno = 1

    while jogador.vida > 0 and adversario.vida > 0:
        print(f"\n=== TURNO {turno} ===")

        jogador.atacar(adversario)

        if adversario.vida <= 0:
            print(f"\n{adversario.nome} foi derrotado!")
            print(f"{jogador.nome} venceu a batalha!")
            break

        adversario.atacar(jogador)

        if jogador.vida <= 0:
            print(f"\n{jogador.nome} foi derrotado!")
            print(f"{adversario.nome} venceu a batalha!")
            break

        turno += 1
   
