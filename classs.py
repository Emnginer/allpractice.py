"""class MyClass:
    x = 10


print(MyClass)"""



#################
"""
class Emon:
    x = 5
p1 = Emon()
p1.y = 10
print(p1.y)"""

######################
"""
class MyClass:
    def move(self):
        print("printed successfullly")

    def draw(self):
        print("python for beginners")


point1 = MyClass()
point1.x = 20
print(point1.x)
point1.draw()
point1.emon()

point2 = MyClass()
point2.x = 30
print(point2.x)
"""

################

"""
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")
    def draw(self):
        print("draw")

P = Point(10, 20)
print(P.x)
print(P.y)
"""

###########################

"""
class Person:

    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi i am {self.name}")

ed = Person("emon das")
print(ed.name)
ed.talk()
"""

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print("talk in english")

p1 = Person("emon", 21 )
print(p1.name)
print(p1.age)

p1.talk()

