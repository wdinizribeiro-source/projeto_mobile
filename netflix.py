class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_plano = ["basic", "premium"]

        if plano in self.lista_plano:
            self.plano = plano
        else:
            raise Exception("Plano inválido")

    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print(f"Pode ver o filme {filme}")
        elif self.plano == "premium":
            print(f"Tá liberado ver o filme {filme}")
        else:
            print("Não pode ver o filme")

    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_plano:
            self.plano = novo_plano


cliente1 = Cliente("Nathan", "nathan@gmail.com", "basic")

print(cliente1.nome)
print(cliente1.plano)

cliente1.ver_filme("Homem-Aranha", "premium")

cliente1.mudar_plano("premium")

print(cliente1.plano)

cliente1.ver_filme("Homem-Aranha", "premium")