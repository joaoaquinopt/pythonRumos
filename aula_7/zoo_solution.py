class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

    def move(self):
        pass

    def eat(self, food):
        pass


class Lion(Animal):
    def make_sound(self):
        return "Arghhh!"

    def move(self):
        return "a correr furiosamente."

    def eat(self, food):
        if food.lower() == "carne vermelha":
            return "a lambuzar-se todo!"
        else:
            return "a pedir um delivery do Chimarrão"


class Elephant(Animal):
    def make_sound(self):
        return "Amendoim!"

    def move(self):
        return "a andar lentamente."

    def eat(self, food):
        if food.lower() == "verduras":
            return "a saborear lenta e demoradamente este manjar"
        else:
            return "a abanar as orelhas energeticamente provocando um furacão na DisneyWorld"


class Penguin(Animal):
    def make_sound(self):
        return "Piu!"

    def move(self):
        return "a andar com passos curtos."

    def eat(self, food):
        if food.lower() == "lavagante":
            return "com o seu smoking natural cheio de nódoas"
        else:
            return "a falar Pinguês furiosamente"


class Zoo:
    def __init__(self, animals):
        self.animals = animals

    def make_animals_make_sounds(self):
        for animal in self.animals:
            print(f"{animal.name} diz: {animal.make_sound()}")

    def make_animals_move(self):
        for animal in self.animals:
            print(f"{animal.name} está {animal.move()}")

    def feed_animals(self):
        food = "lavagante"
        print(f"O tratador vai alimentar os animais com {food}")
        for animal in self.animals:
            print(f"{animal.name} está {animal.eat(food)}")


animals = [Lion("Simba"), Elephant("Babar"), Penguin("Pingu")]

zoo = Zoo(animals)

zoo.make_animals_make_sounds()
zoo.make_animals_move()
zoo.feed_animals()