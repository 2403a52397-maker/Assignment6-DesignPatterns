
# Factory Pattern - Travel Booking System

class Travel:
    def book(self):
        pass


class Flight(Travel):
    def book(self):
        print("Flight ticket booked successfully.")


class Train(Travel):
    def book(self):
        print("Train ticket booked successfully.")


class Bus(Travel):
    def book(self):
        print("Bus ticket booked successfully.")


class TravelFactory:
    @staticmethod
    def get_travel(choice):
        if choice == "flight":
            return Flight()
        elif choice == "train":
            return Train()
        elif choice == "bus":
            return Bus()
        else:
            return None


choice = input("Enter travel type (flight/train/bus): ").lower()

travel = TravelFactory.get_travel(choice)

if travel:
    travel.book()
else:
    print("Invalid travel type.")
```