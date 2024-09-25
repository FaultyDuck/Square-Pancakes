# Object Oriented Programming (OOP)

class Vehicle:
    wheels = 0;
    seats = 0;
    engine = 0;

    def __init__(self, wheels, seats, engine): #arguments, parameters, from functions
        self.wheels = wheels #refering to self attibutes
        self.seats = seats
        self.engine = engine

    def get_wheels(self):
        return self.wheels
    
car = Vehicle(4, 5, 1) #3 numbers are assigned as wheels seats and engine
print(car.get_wheels())