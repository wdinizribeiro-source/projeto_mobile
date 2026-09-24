from classe import Vendedor


# vendedor = "Nathan"
# vendas = 1000
# meta = 500

# if vendas >= meta:
#     print(f"{vendedor} bateu a meta")

# else:
#     print(f"{vendedor} não  bateu a meta")

#     # --------------------------- Usando POO --------------------------




vendedor1 = Vendedor('nathan')
print(vendedor1.nome)
vendedor1.vendeu(1000)
vendedor1.bateu_meta(500)

vendedor2 = Vendedor('joao')
print(vendedor2.nome)
vendedor2.vendeu(400)
vendedor2.bateu_meta(401)
