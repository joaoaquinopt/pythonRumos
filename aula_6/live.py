class Car:
    def __init__(self, brand, key_pattern, serial):
        self.brand = brand
        self.seats = 5
        self.colour = "black and yellow"
        self.__key_pattern = key_pattern
        self._serial = serial

    @property
    def key_pattern(self):
        return str(self.__key_pattern)[:1] + "***"

    @key_pattern.setter
    def key_pattern(self, new_key):
        if len(str(new_key)) < 5:
            self.__key_pattern = new_key

    def get_key_pattern(self):
        return str(self.__key_pattern)[:1] + "***"

    def set_key_pattern(self, new_key):
        if len(str(new_key)) < 5:
            self.__key_pattern = new_key


car = Car("ferrari", 1231, "1234123")
car.set_key_pattern(34645454)
print(car.get_key_pattern())
print(car.seats)
print(car._Car__key_pattern)