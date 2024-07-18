class Engine:
    def __init__(self, power):
        self.power = power


class Wheels:
    def __init__(self, total):
        self.total = total


class Seats:
    def __init__(self, total, material):
        self.total = total
        self.material = material


class Car:
    def __init__(self, power, seats_number, seats_material):
        self.engine = Engine(power)
        self.seats = Seats(seats_number, seats_material)
        self.wheels = Wheels(4)


class Car:
    def __init__(self, engine, seats_number, seats_material):
        self.engine = engine
        self.seats = Seats(seats_number, seats_material)
        self.wheels = Wheels(4)


class Bicycle:
    def __init__(self, seats_material):
        self.seats = Seats(1, seats_material)
        self.wheels = Wheels(2)


class Boat:
    def __init__(self, power, seats_number, seats_material):
        self.engine = Engine(power)
        self.seats = Seats(seats_number, seats_material)
