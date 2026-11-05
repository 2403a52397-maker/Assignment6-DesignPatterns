# Factory Pattern - Vehicle Factory

class Vehicle:
    def drive(self):
        pass


class Car(Vehicle):
    def drive(self):
        print("Driving a car.")


class Bike(Vehicle):
    def drive(self):
        print("Riding a bike.")


class Truck(Vehicle):
    def drive(self):
        print("Driving a truck.")


class VehicleFactory:
    @staticmethod
    def get_vehicle(choice):
        if choice == "car":
            return Car()
        elif choice == "bike":
            return Bike()
        elif choice == "truck":
            return Truck()
        else:
            return None


choice = input("Enter vehicle (car/bike/truck): ").lower()

vehicle = VehicleFactory.get_vehicle(choice)

if vehicle:
    vehicle.drive()
else:
    print("Invalid vehicle type.")
```