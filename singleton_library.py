# Singleton Pattern - Library Management System

class Library:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def display(self):
        print("Library management system is running.")


library1 = Library()
library2 = Library()

library1.display()

print("Same instance:", library1 is library2)
```