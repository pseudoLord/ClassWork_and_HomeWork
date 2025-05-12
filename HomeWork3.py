class Dog:
    print("Гав! (привіт)")
    def __init__(self, bone="Гризти кістку", bool="Гратись з м'ячиком", twodog="Гавкати на собаку", runbool="бігти за м'ячиком"):
        self.bone = bone
        self.bool = bool
        self.twodog = twodog
        self.runbool = runbool

dog = Dog()
print(f" Собака побачив другу собаку: {dog.twodog}")
print(f" У собаки є кістка: {dog.bone}")
print(f" Собакі кинули м'яч: {dog.runbool}")
print(f" Собака догнав м'яч: {dog.bool}")