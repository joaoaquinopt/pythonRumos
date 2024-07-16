'''
No ficheiro zoo.py criar 3 classes de Animais partindo da Classe
Animal.
Completar os métodos da classe Zoo e criar o zoo_logical.

'''


class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

    def move(self):
        pass

    def eat(self, food):
        pass


class Zoo:
    def __init__(self, animals):
        self.animals = animals

    def make_animals_make_sounds(self):
        for animal in self.animals:  ## list = [Cachorro, Gato, Passaro]
            animal.make_sound()

    def make_animals_move(self):
        for animal in self.animals:  ## list = [Cachorro, Gato, Passaro]
            animal.move()

    def feed_animals(self):
        for animal in self.animals:  ## list = [Cachorro, Gato, Passaro]
            animal.eat()


class Cachorro(Animal):

    def make_sound(self):
        print("Woof")

    def move(self):
        print("Sit")

    def eat(self):
        print("Pizza")


class Gato(Animal):

    def make_sound(self):
        print("Miau")

    def move(self):
        print("Rool")

    def eat(self):
        print("Bolachas")


class Passaro(Animal):

    def make_sound(self):
        print("PiuPiu")

    def move(self):
        print("Fly")

    def eat(self):
        print("Racao")


rex = Cachorro("Rex")
mia = Gato("Mia")
piu = Passaro("Piuu")

animals = Zoo([mia])

animals.make_animals_make_sounds()
animals.make_animals_move()
animals.feed_animals()
