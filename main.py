class Car:
    def __init__(self, make, model, year, weight, num_doors):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.num_doors = num_doors

    def display_info(self):
        print(f"Make: {self.make}\nModel: {self.model}\nYear: {self.year}\nWeight: {self.weight}\nNumber of doors: {self.num_doors}")

    def honk(self):
        print("HONK")

aCar = Car("Dodge", "Vroom", 2052, 3042.1, 12)
aCar.display_info()
aCar.honk()

class Boat:
    def __init__(self, make, model, year, weight, boat_type):

        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.boat_type = boat_type
        print("A boat has been created!")

    def display_info(self):
        print(
            f"Make: {self.make}\nModel: {self.model}\nYear: {self.year}\nWeight: {self.weight}\nBoat Type: {self.boat_type}")

    def honk(self):
        print("BOOOOP")


aBoat = Boat("BloopBloop", "UndaDaSea", 1864, 8, "Submarine")
aBoat.display_info()
aBoat.honk()

class Truck:
    def __init__(self, make, model, year, weight, num_doors, payload_capacity):

        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.num_doors = num_doors
        self.payload_capacity = payload_capacity
        print("A truck has been created!")

    def display_info(self):
        print(
            f"Make: {self.make}\nModel: {self.model}\nYear: {self.year}\nWeight: {self.weight}\nNumber of doors: {self.num_doors}\nPayload capacity: {self.payload_capacity}")

    def honk(self):
        print("BRRRRRR")

    def dump_load(self):
        print("Load has been duuumped!")

aTruck = Truck("BIG", "BOI", 1776, 10000, 45, 1000000)
aTruck.display_info()
aTruck.honk()
aTruck.dump_load()