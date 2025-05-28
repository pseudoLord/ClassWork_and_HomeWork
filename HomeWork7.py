import math

try:
    result = math.cube(3)
    print(result)
except AttributeError:
    print("Функція 'cube' не знайдена в модулі math")
