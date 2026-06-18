class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"Vehicle Make: {self.make}")
        print(f"Vehicle Model: {self.model}")

class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        # Call the parent class constructor
        #super().__init__(make, model)
        self.num_doors = num_doors

    def display_info(self):
        # Call the parent method first
        #super().display_info()
        print(f"Number of Doors: {self.num_doors}")

# Create a Vehicle instance
vehicle = Vehicle("Toyota", "Corolla")
vehicle.display_info()

print()  # Just to separate outputs

# Create a Car instance
car = Car("BMW", "X5", 4)
car.display_info()