# Imagine I want to list these vechicles on craigslist
''' Parent Class '''
class Vehicle:

    def __init__(self, make, model, color, year, mileage) -> None:
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.mileage = mileage
    
    def honk(self):
        return "BEEEP BEEEP"
    
    def drive(self, miles_driven):
        self.mileage += miles_driven
        return self.mileage
    
    def __repr__(self) -> str:
        return f'A {self.color} {self.year} {self.make} {self.model} with {self.mileage} miles.'
    
if __name__ == '__main__':
    my_vehicle = Vehicle('Toyota', 'Camry', 'gray', 2015, 6000)

    print(my_vehicle.make)
    print(my_vehicle.mileage)

    print(my_vehicle.honk())
    print(my_vehicle.drive(1234))
    print(my_vehicle.mileage)
    print(my_vehicle)

# Create child class
# convertible class inherits from vehicle
class Convertible(Vehicle):

    def __init__(self, make, model, color, year, mileage, top_down=True) -> None:
        super().__init__(make, model, color, year, mileage)
        self.top_down = top_down
    
    def change_top_status(self):
        if self.top_down:
            self.top_down = False
            return 'Top is now up'
        else:
            self.top_down = True
            return "Top is now down"
    
    def __repr__(self) -> str:
        return f'A  convertible {self.color} {self.year} {self.make} {self.model} with {self.mileage} miles. Is it true the top is down? {self.top_down}'
    
if __name__ == '__main__':
    my_vehicle = Convertible('Toyota', 'Camry', 'gray', 2015, 6000, top_down=False)

    print(my_vehicle.make)
    print(my_vehicle.mileage)

    print(my_vehicle.honk())
    print(my_vehicle.drive(1234))
    print(my_vehicle.mileage)
    print(my_vehicle)

    print(my_vehicle.top_down)
    print(my_vehicle.change_top_status())
    print(my_vehicle.top_down)

    print(my_vehicle.honk())
    print(my_vehicle.drive)