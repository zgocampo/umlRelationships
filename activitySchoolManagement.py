#Exercise 1
class Person:
    def __init__(self,name,age):
        self.age = age
        self.name = name

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

person1 = Person("mike",67)
person1.display_info()