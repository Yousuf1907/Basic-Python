class Mammal:
    def walk(self):
        print('walk')


class Cat(Mammal):
    pass

Cat.walk(Mammal)
