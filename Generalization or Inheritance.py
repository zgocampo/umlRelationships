class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

# Example Usage
if __name__ == "__main__":
    dog = Dog("Buddy")
    print(f"[Generalization] {dog.name} says: {dog.make_sound()}")