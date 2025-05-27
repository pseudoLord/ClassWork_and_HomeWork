class Animal:
    def __init__(self, name, drink, eat, sleeptime, play):
        self.name = name
        self.drink = drink
        self.eat = eat
        self.sleeptime = sleeptime
        self.play = play

    def __str__(self):
        return (f"{self.name} їсть {self.eat}, п'є {self.drink}мл, спить {self.sleeptime} год., грає в {self.play}")


class Dog(Animal):
    def __init__(self):
        super().__init__(name = "Собака", eat = "мясо", drink = 900, sleeptime = 8, play = "м'ячик")


class Cat(Animal):
    def __init__(self):
        super().__init__(name = "Кіт", eat = "рибу", drink = 700, sleeptime = 15, play = "миша")


dog = Dog()
cat = Cat()
hamster = Animal(name="Хом'як", eat="зерно", sleeptime=10, drink=100, play="бігове колесо")

print(dog)
print(cat)
print(hamster)