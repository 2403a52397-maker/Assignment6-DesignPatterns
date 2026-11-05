# Singleton Pattern - Exam Management System

class Exam:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def conduct_exam(self):
        print("Exam is being conducted.")


exam1 = Exam()
exam2 = Exam()

exam1.conduct_exam()

print("Same instance:", exam1 is exam2)
```