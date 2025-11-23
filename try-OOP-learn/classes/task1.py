class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
    def make_sound(self):
        match self.species:
            case "Dog": return "WOOF"
            case "Cat": return "MEOW"
            case _: return "Making sound~~"

Mako = Animal("Mako", species="Cat", age=15)
print(Mako.make_sound())
BoLin = Animal("BoLin", species="Dog", age=15)
print(BoLin.make_sound())
Kora = Animal("Kora", species="AVATAR", age=15)
print(Kora.make_sound()
#yes. yesterday i watched the last episode of The Legend of Korra. How u guess