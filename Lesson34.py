class Student:
    print("Hi!")
    def __init__(self, height=160, age=11):
        self.height = height
        self.age = age
        print("I am alive")
    def grow (self, height=1):
        self.height += height
    def sleep (self, height=1):
        self.height += height

first_student = Student()
print(f" First Student height {first_student.height}")
second_student = Student()
print(f" Second Student height {second_student.height}")
second_student.grow(15)
print(f" Second Student height after growth {second_student.height}")
tree_student = Student()
print(f" Tree Student height {tree_student.height}")
tree_student.sleep()
tree_student.sleep()
tree_student.sleep()
print(f" Tree Student height after sleep {tree_student.height}")

class Squidward:
    print("Hi, I am Squidward!")
    def __init__(self, height=176, age=29, work="cashier", bestfr="spangebob", friend="patrik"):
        self.height = height
        self.age = age
        self.work = work
        self.bestfr = bestfr
        self.friend = friend


octopus = Squidward(height=178, age=30, work="cashier", bestfr="spangebob", friend="patrik")
print(octopus.height, octopus.age, octopus.work, octopus.bestfr, octopus.friend)
