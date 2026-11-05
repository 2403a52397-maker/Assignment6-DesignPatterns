# Factory Pattern - Food Ordering System

class Food:
    def prepare(self):
        pass


class Pizza(Food):
    def prepare(self):
        print("Preparing Pizza.")


class Burger(Food):
    def prepare(self):
        print("Preparing Burger.")


class Biryani(Food):
    def prepare(self):
        print("Preparing Biryani.")


class FoodFactory:
    @staticmethod
    def get_food(choice):
        if choice == "pizza":
            return Pizza()
        elif choice == "burger":
            return Burger()
        elif choice == "biryani":
            return Biryani()
        else:
            return None


choice = input("Enter food (pizza/burger/biryani): ").lower()

food = FoodFactory.get_food(choice)

if food:
    food.prepare()
else:
    print("Invalid food choice.")
```