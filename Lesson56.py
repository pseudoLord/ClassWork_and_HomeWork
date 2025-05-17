import random

class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.home = home
        self.car = car

    def get_home(self):
        pass

    def get_car(self):
        pass

    def get_home(self):
        pass

    def eat(self):
        pass

    def work(self):
        pass

    def shopping(self, manage):
        pass

    def chill(self):
        pass

    def clean_home(self):
        pass

    def repair_car(self):
        pass

    def day_indexes(self, day):
        pass

    def is_alive(self):
        pass

    def live(self, day):
        pass


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.flue = brand_list[self.brand]["flue"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.flue >= self.consumption:
            self.strength -= 1
            return True
        else:
            print("Car can not move")
            return False

brands_of_car = {
    "BMW": {"flue": 100, "strength": 100, "consumption": 6},
    "Lada": {"flue": 50, "strength": 40, "consumption": 10},
    "Renoult": {"flue": 70, "strength": 150, "consumption": 8},
    "Ferrari": {"flue": 80, "strength": 120, "consumption": 14},
}

class House:
    def __init__(self):
        self.mess = 0
        self.eat = 0


class Job:
    def __init__(self, jobs_list):
        self.job = random.choice(list(jobs_list))
        self.salary = jobs_list[self.job]["salary"]
        self.gladness_less = jobs_list[self.job]["gladness_less"]


job_list = {
    "Java Developer": {"salary": 50, "gladness_less": 10},
    "Python Developer": {"salary": 40, "gladness_less": 3},
    "C++ Developer": {"salary": 45, "gladness_less": 15},
    "QA": {"salary": 38, "gladness_less": 1},
}

def get_home(self):
    self.home = House()


def get_car(self):
    self.car = Auto(brands_of_car)


def get_job(self):
    if self.car.drive():
        pass
    else:
        self.repair_car()
        return
    self.job = Job(job_list)


def eat(self):
    if self.home.food <= 0:
        self.shopping("food")
    else:
        if self.satiety >= 100:
            self.satiety = 100
            return
        self.satiety += 5
        self.home.food -= 5
