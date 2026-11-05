# Singleton Pattern - University Management System

class University:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def display(self):
        print("University management system is running.")


university1 = University()
university2 = University()

university1.display()

print("Same instance:", university1 is university2)
```