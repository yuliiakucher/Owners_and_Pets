
class Pet:
    def __init__(self, name, age, type):
        self.name = name.title()
        self.age = int(age)
        self.type = type.title()

    def __repr__(self):
        return str(self.__dict__)

    def __str__(self):
        return str(self.__dict__)

class Owner:
    def __init__(self, name, age, city):
        self.name = name.title()
        self.age = int(age)
        self.city = city.title()
        self.pets = []

    def __repr__(self):
        return str(self.__dict__)

    def __str__(self):
        return str(self.__dict__)

    def add_pet(self, name, age, type):
        self.pets.append(Pet(name, age, type))

    def del_pet(self, index):
        del self.pets[index]
