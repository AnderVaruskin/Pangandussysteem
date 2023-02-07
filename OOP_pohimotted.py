class Dog:
    def __init__(self, name):
        self.name = name

    def add_one(self, x):
        return x + 1

    def bark(self):
        print("Bark")

d = Dog("Tim")
d2 = Dog("Bill")
