#Exercise 1
class Person:
    def __init__(self,name,age):
        self.__age = age
        self.name = name

    def get_age(self):
        return self.__age
person = Person("LINA", 20)

print(f"Name: {person.name}")
print(f"Age: {person.get_age()}")

#IT is better to access __age by get_age becuase it allows you to control how data is accessed and modified