'''
Objetivo
A partir das 3 classes (que representam componentes de veículos)
existentes no ficheiro vehicles, criar 3 classes de veículos diferentes
compostas por esses componentes.
Os elementos que compõem os veículos devem ser impressos na
consola.

'''


class Engine:
    def __init__(self, power):
        self.power = power

    def __str__(self):
        return "Engine power is " + str(self.power)


class Wheels:
    def __init__(self, total):
        self.total = total

    def __str__(self):
        return "We have " + str(self.total) + " wheels"


class Seats:
    def __init__(self, seats_total, material):
        self.seats_total = seats_total
        self.material = material

    def __str__(self):
        return "We have " + str(self.seats_total) + "seats with " + str(self.material)


class Car:
    def __init__(self, power, total):
        self.engine = Engine(power)
        self.seats = Seats(total, "leather")
        self.wheels = Wheels(4)


class Bus:
    def __init__(self, power, total, seats_total, material):
        self.engine = Engine(power)
        self.wheels = Wheels(total)
        self.seats = Seats(seats_total, material)


car = Car(10, 4)
print(car.seats)

bus = Bus(1000, 4, 4, 'Hello')
print(bus.engine,  bus.wheels,  bus.seats)
