class Vehicle:
    def vehicle(self):
        print("I am a vehicle")

class FourWheeler(Vehicle):
    def fourwheeler(self):
        print("I have four wheels")

class Car(FourWheeler):
    def car(self):
        print("I am a car")


# Object creation
c = Car()

# Invoking methods
c.car()
c.fourwheeler()
c.vehicle()