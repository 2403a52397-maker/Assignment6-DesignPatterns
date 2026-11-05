# Singleton Pattern - Hospital Management System

class Hospital:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def display(self):
        print("Hospital management system is running.")


hospital1 = Hospital()
hospital2 = Hospital()

hospital1.display()

print("Same instance:", hospital1 is hospital2)
```