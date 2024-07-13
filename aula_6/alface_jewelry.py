class Jewel:
    def __init__(self, kind, material, price):
        self.kind = kind
        self.material = material
        self.price = price

    def is_a(self):
        return self.kind

    def made_with(self):
        return self.material

    def it_costs(self):
        return self.price


first_jewel = Jewel("Colar", "Ouro", 20000)
second_jewel = Jewel("Brinco", "Prata", 5000)
third_jewel = Jewel("Relogio", "Ouro", 30000)

print(f"A primeira joia é um {first_jewel.kind} o material é {first_jewel.material} e o preço é:{first_jewel.price}")

jewels = [first_jewel, second_jewel, third_jewel]

for jewel in jewels:
    jewel.is_a()
    jewel.made_with()
    jewel.it_costs()
    print(f'Essas são as joias que tenho para oferecer: {jewel.is_a()} de {jewel.made_with()} por {jewel.it_costs()}')

