'''
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self._age = age
        self.__city = city
        person_john = Person("John", 22, “Mira”)

# public access
print(person_john.name)
# private access
print(person_john._age)
# private access by name mangling
'''


class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name


person = Person('Rui')
print(person.name)
person.name = 'Ivo'
print(person.name)
