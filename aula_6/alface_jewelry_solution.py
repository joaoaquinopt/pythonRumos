class Jewel:
    def __init__(self, kind, material, price):
        self.kind = kind
        self.material = material
        self.price = price

    def is_a(self):
        print(f"This jewel is a: {self.kind}")

    def made_with(self):
        print(f"This jewel is made with: {self.material}")

    def it_costs(self):
        print(f"This jewel costs: ${self.price}")


jewel1 = Jewel("Ring", "Gold", 500)
jewel2 = Jewel("Necklace", "Silver", 300)
jewel3 = Jewel("Earring", "Diamond", 800)

jewels = [jewel1, jewel2, jewel3]

print("Here is our jewels: ")
print("-" * 20)
for jewel in jewels:
    jewel.is_a()
    jewel.made_with()
    jewel.it_costs()
    print("-" * 20)
