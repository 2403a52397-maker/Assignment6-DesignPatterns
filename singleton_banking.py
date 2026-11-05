# Singleton Pattern - Banking System

class Bank:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def display(self):
        print("Bank system is running.")


bank1 = Bank()
bank2 = Bank()

bank1.display()

print("Same instance:", bank1 is bank2)
```