class Person:

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
       return f"Hello, my name is {self.firstname} {self.lastname} and I’m {self.age} years old"


human = Person("Roman", "Povzyk", "29")
print(human.talk())