class Animal:
    def __init__(self, name):
        self.name = name
        self.sound = ""
    
    def make_sound(self):
        print(f"{self.name} says: {self.sound}")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.sound = "Woof Woof!"

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.sound = "Meow Meow!"

# Test
dog = Dog("Rex")
cat = Cat("Mimi")
dog.make_sound()
cat.make_sound()
