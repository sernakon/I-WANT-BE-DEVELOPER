class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
class Car(Vehicle):
    fuel_type = None

class Motorcycle(Vehicle):
    helmet = None
class Bicycle(Vehicle):
    bicycle_pedals=None


a = Car("Yamaha", "Y2K", 2006)
a.fuel_type = 95
print(a.fuel_type)