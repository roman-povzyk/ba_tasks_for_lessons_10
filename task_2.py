class Dog:

    age_factor = 7

    def __init__(self):
        self.dog_age = int(input("Введіть вік пса\n"))

    def human_age(self):
        return self.dog_age * self.age_factor


math = Dog()
print(math.human_age())