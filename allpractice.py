# print('hello world')
#
# x = 10
# x += 2
# print(x)
#
# name = (input('What is your name?: '))
# age = (input('what is your age?: '))
#
# a = f'{name} is a {age} years old'
# print(a)
#
#
# course = 'python for beginners'
#
# print(course)
# print(len(course))
# print(course.upper())
# print(course.lower())
# print(course.find('f'))
# print(course.replace('beginners','absolute beginners'))
# print('zython' in course)
# print('for' in course)
#
# weight = input('weight in pounds: ')
# kilograms = int(weight) * 0.45

#
#
#
# weight = input('weight: ')
#
# unit = input('(L)bs or (K)g: ')
#
# if unit.upper() == 'L':
#     converted = int(weight) * 0.45
#     print(f'you are {converted} kilos')
# else:
#     converted = int(weight) / 0.45
#     print(f'you are {converted} pounds')

#
# print("hello world")
#
# a = 4
# b = 6
# print(a+b)
#
#
#
# course = "Python for begineers"
# print(course)
# print(len(course))
# print(course.upper())
# print(course.lower())
# print(course.replace('Python', 'PYTHON' ))
# print(course.find('f'))
#
# print(course[3:-3])
#
# print("For" in course)

#
# print(course.title())

#
# has_high_income = True
# has_good_credit = True
#
# if has_good_credit or  has_high_income :
#     print('eligible for loan')
# else:
#     print('you are not eligible for loan')

#
# name = input('enter your name: ')
#
# if len(name) < 3:
#     print('name at least 3 character long')
# elif len(name) > 50 :
#     print('name must be maximum of 50 character')
# else:
#     print('name looks good')


# weight converter
'''
weight = input('weight: ')
unit = input("(L)bs or (K)g: ")


if unit.upper() == 'L':
    converted = int(weight) * 0.45
    print(f"you are {converted} kilos")

else:
    converted = int(weight) / 0.45
    print(f"you are {converted} pounds")

'''
'''
secret_number = 4

guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You won!')
        break

else:
    print('Sorry! you failed')
'''
#################################################
'''
command = ''
started = False

while True:

    command = input('> ').lower()
    if command == "help":

        print("""
   start- to start the car
   stop- to stop the car
   quite- to quite
        """)

    elif command == "start":
        if started:
            print("car is already started")
        else:
            started = True
            print("car started")
    elif command == "stop":
        if not started:
            print('car is already stopped')
        else:
            started = False
            print("car stopped")
    elif command == "quite":
        break
    else:
        print("Sorry! I don't understand that")
'''
########################################################
"""
for s in range(3):
    for f in range(4):
        print(f"({s}, {f})")
"""

################################################

"""

command = ''
started = False
while command != "quite":
    command = input(">>> ").lower()
    if command == "help":
        print('''
        start - to start the car 
        stop - to stop the car
        quite - to quite

        ''')
    elif command == 'start':
        if started :
            print('car is already started')
        else:
            started = True
            print('car started')
    elif command == 'stop':
        if not started:
            print('car is already stopped')
        else:
            started = False
            print('car stopped')
    elif command == 'quite':
        break
    else:
        print('sorry i dont understand that')

"""

"""number = [10,20,30,40]

total = 0

for i in number:
    total += i
print(total)"""

"""
number = [10,20,30,40]

for count in number:
    output = ""
    for x_count in range(count):
        output += 'x'
    print(output)
"""

"""
num = [1,2,3,4,5,6,7,8,9,10]

for i in num:
    if i % 2 == 0:
        print(i)"""

"""
for i in range(1,10):
    if i % 2 == 1:
        print(i)
"""

"""
i = 1

while i < 100:
    if i % 2 == 1:

        print(i)
    i+=1"""

"""
num = [2,3,4,5,5,8,1,9]

max = num[0]

for count in num:
    if count > max:
        max = count
print(max)"""

"""
num=[20,30,20]

total = 0

for i in num:
    total += i
print(total)"""

"""
num=[20,30,20]

total = 0

for i in num:
    total += i
print(total)"""

"""
for i in range(5):
    for u in range(4):
        print(i,u)"""

"""
course = "emon das"
print(len(course))
print(course.capitalize())
print(course.upper())
print(course.lower())
print(course.replace('das' , 'kanti das'))
print("emom" in course)
"""
"""import math

print(math.floor(2.9))
print(math.ceil(2.9))

print(round(2.6))
print(abs(-2.3))"""

"""
name = input("enter your name: ")

if len(name) < 3 :
    print("name must be at least 3 characters")
elif len(name) > 50 :
    print("name can be maximum of 50 characters")
else:
    print("name looks good")
"""

"""
weight = int(input("weight: "))
unit = input("(L)bs or (K)g")

if unit == "L" :
    converted = weight * 0.45
    print(f'you are {converted} pounds')
else :
    converted = weight / 0.45
    print(f'you are{converted} kilos')"""

"""i = 2
while i < 10 :
    print(i)
    i+=1"""

""""secret_number = 3
guess_count = 0
guess_limit = 3

while guess_count < guess_limit :
    guess = int(input("number: "))
    guess_count += 1

    if guess == secret_number :
        print("you won !")
        break
else:
    print("sorry you failed! try again")"""

"""
command = ""
started = False
while command != 'quite' :
    command = input("> ").lower()
    if command == "help" :
        print('''
            start - to start the car
            stop - to stop the car
            quite - to quite the car
        ''')
    elif command == "start" :
        if started :
            print("car is already started")
        else :
            started = True
            print("car started")
    elif command == "stop" :
        if not started :
            print("car is already stopped")
        else :
            started = False
            print('car stopped')
    elif command == "quite":
        break
    else:
        print("sorry, i do not understand")
"""

"""i =1
while i < 100 :
    if i % 2 == 1:
        print(i)
    i+=1
"""

"""prices = [10,20,20,40]

total = 0

for price in prices :
    total += price
print(total)"""
"""
item = [5,2,5,2,2]
for num in item :
    output = ""
    for num2 in range(num):
        output += 'x'
    print(output)
"""

"""numbers = [2,3,4,9,7,11]
max = numbers[0]

for number in numbers:
    if number > max :
        max = number
print(max)"""

"""numbers = [3,4,9,7,11]
min = numbers[0]

for number in numbers:
    if number < min :
        max = number
print(min)


numbers = [1,3,4,9,7,11]
min = numbers[0]

for number in numbers:
    if min < number :
        number = min
print(min)"""

"""list =[2,4,5,5,1,2,6,8,7]
num =[]

for item in list:
    if item not in num:
        num.append(item)
print(num)
"""

""""coordinates = [1,3,4]

x,y,z = coordinates
print(x,z)"""

"""
customer = {
    "name" : "emon",
    "age" : 22,
    "phone" : "015791345",
    'is_verified' : True
}
print(customer.get("birthdate" , "nov 16 2000"))"""

"""phone = input("phone: ")
digits_mapping ={
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five",
    "6" : "Six",
    "7" : "Seven",
    "8" : "Eight",

    "0" : "Zero"
}
output = ""
for ch in phone :
    output += digits_mapping.get(ch, "m") + " "
print(output)
"""

"""def user() :

    message = input('> ')
    words = message.split()
    emojis ={
        ":)" : "😊",
        ":(" : "☹"
    }
    output = ""
    for word in words:
        output += emojis.get(word , word) + ' '
    print(output)


user()"""

"""def user(first_name, last_name):

    print(f"Hi {first_name} {last_name}")


user(last_name="emon", "das")"""

"""def multi(num):
    return num + num
print(multi(3))"""
""""
def emoji_converter(message):
    words = message.split()
    emojis = {
        ":)": "😊",
        ":(": "☹"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + ' '
    return output

message = input('> ')
print(emoji_converter(message))"""

"""try:
    age = int(input("age: "))
    print(age)
except ValueError:
    print("you know that age is a number. it can not be a string float or something")"""

"""class Point:


    def move(self):
        print("this is the move part")
    def drawq(self):
        print("and this is the draw part")


point1 = Point() #creating new object
point1.x = 10
print(point1.x) # x is attribute like creating new object
point1.move()

point2 = Point()
point2.y=20
print(point2.y)
point2.drawq()
"""

"""class User:


    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("this is the moving part")
    def draw(self):
        print("this is the drawing part")


obj1 = User(104 , 20)
print(obj1.x)
print(obj1.y)
obj1.draw()


class MyClass:
    x = 5
    y = 6
    c = x + y

p = MyClass()
print(p.c)"""

"""
class Person:


    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("emon" , "230")

p1.age = 30
print(p1.name)
print(p1.age)
"""

"""
class Person:


    def __init__(self,name,age):
        self.name = name
        self.age = age

    def Mymethod(self):
        print("my name is " + self.name)


p1 = Person("emon" , "22")

print(p1.name)
print(p1.age)

p1.Mymethod()"""

"""class Person:


    def __init__(self, name):
        self.name = name

    def talk(self):
        print("hi my name is " + self.name)


p1 = Person("emon das")

print(p1.name)
p1.talk()"""

"""class Mammal:
    def bark(self):
        print("hey this is the walk part")

    def miu(self):
        print("cat is screaming")

class dog(Mammal):
   pass


class cat(Mammal):
    pass


dog1 = dog()
dog1.miu()
dog2 = cat()
dog2.bark()"""

"""class Person:

    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

class Name(Person):
    pass

p1 = Name("emon", "das")
print(p1.lastname)
"""

"""
class Person:
    def name1(self):
        print("emon")

class Student(Person):

    def stuname(self):
        print("rahimkarimabdul")


p = Student()
p.stuname()
p.name1()
"""

"""def num(a,b):
    return a * b

print(num(2,4))"""

""""class Person:

    def __init__(self, fname, lname ):
        self.firstname = fname
        self.lastname = lname

class Name(Person):


    def __init__(self, fname, lname,year):
        Person.__init__(self, fname, lname)
        self.newYear = year


p1 = Name("emon", "das", 22022)
print(p1.newYear)
"""

"""
def kg_to_lbs(weight):
    return weight * 0.45

def lbs_to_kg(weight):
    return weight / 0.45

"""

"""import converter

from converter import lbs_to_kg

print(lbs_to_kg(70))

print(converter.lbs_to_kg(70))
print(converter.kg_to_lbs(160))"""

"""class MainPerson:

    def move(self):
        print("move this")

class Person(MainPerson):
    pass
"""

"""
from converter import Person

p1 = Person()
p1.move()
p1.walk()
"""

"""
customer = {
    "name" : "emon das",
    "age" : 20,
    "is_varified" : True

}

print(customer.get("birthdate"))"""

"""
def user(a,b):

   return a * b

print(user(2,5))
"""

"""phone = input("phone: ")
digits = {
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "six",
    "7" : "seven",
}
output = ""
for user in phone:
    output += digits.get(user, "!") + " "
print(output)
"""

"""message = input("> ")
text = message.split()

emojis = {
    ":)" : '😊',
    ":(" : "☹"
}
output = ""
for user in text :
    output += emojis.get(user, user) + " "
print(output)"""

"""
def emoji_converter(message):

    text = message.split()

    emojis = {
        ":)" : '😊',
        ":(" : "☹"
    }
    output = ""
    for user in text :
        output += emojis.get(user, user) + " "
    return output

message = input("> ")
print(emoji_converter(message))"""

"""
class Point:
    def move(self):
        print("moving part")

    def draw(self):
        print("drawing part")


p1 = Point()
p1.x = 20
print(p1.x)
p1.move()
p1.draw()
"""

"""class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("moving part")

    def draw(self):
        print("drawing part")


p1 = Point(20, 30)
p1.draw()
print(p1.y)"""

'''class Person:

    def __init__(self, name ):
        self.name = name


    def talk(self):
        print("talk")

p1 = Person("emon")
print(p1.name)'''

"""
class Person:
    def move(self):
        print("moving part")

    def draw(self):
        print("drawing part")

class Point(Person):
    pass

class Point2(Person):
    pass


p1 = Point()
p1.move()

p2 = Point2()
p2.draw()

p3 = Person()
p3.draw()
p3.move()
"""

"""
secret_number = 9

guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("guess: "))
    guess_count += 1
    if guess == secret_number:
        print("you won")

        break

else:
    print("try again")"""

"""
i = 1
while i < 20 :
    if i % 2 == 0:

        print(i)
    i +=1
"""

"""
class Person():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self ):
        print("moving part")
        print(f"hi, i am {self.x} years old")

    def draw(self):
        print("drawing part")


p1 = Person(30, 20)

print(p1.x)
print(p1.y)
p1.move()
p1.draw()

"""

"""class Person:

    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"hey {self.name} you are talking like  an idiot")


p2 = Person("Emon ")
p2.talk()
"""

"""class mamal:
    def walk(self):
        print("walk")

    def draw(self):
        print("draw")

class dog(mamal):
    pass


class cat(mamal):
    pass


dog1 = dog()
dog1.walk()
"""

""""
import converter

from converter import kg_to_lbs

print(kg_to_lbs(50))

print(converter.lbs_to_kg(50))"""

"""from converter import find_max

numbers = [2, 9, 5, 3, 8, 6]

print(find_max(numbers))"""

# fffffffffffffff
"""
import ecommerce.shipping 

ecommerce.shipping.calc_shipping() """

"""from ecommerce import shipping

shipping.calc_shipping()
"""

"""from ecommerce.shipping import calc_shipping


calc_shipping()"""

"""for i in range(3):
    print(random.random())
    print(random.randint(10,20))
"""

"""members = ["emon", "mosh", "rahim", "karim"]

leader = random.choice(members)

print(leader)
"""

"""
(1,6)
(2,5)
(5,3)
(6,5)
(2,4)

like that
"""

"""class Dice:
    def roll(self):
        first = random.randint(1,8)
        second = random.randint(1,8)
        return (first, second)


dice = Dice()
print(dice.roll())"""

# path.mkdir()
# path.exits()
# path.rmdir()

"""from pathlib import Path

path = Path()

for file in path.glob("*.py"):
    print(file)
"""

"""from pathlib import Path

path = Path()

for files in path.glob("*.py"):
    print(files)
"""

"""message = input("> ")

test = message.split()
emoji = {
    ":)" : "😊",
    ":(" : "😊"
}

output = ""
for messages in test:
    output += emoji.get(messages , messages) + " "
print(output)
"""

"""
path = Path("E-commerce")

print(path.rmdir())
print(path.mkdir())
print(path.exits())
"""
"""
path = Path()

for file in path.glob("*.*"):
    print(file)"""

"""import random

class Dice:

    def roll(self):
        
        first = random.randint(1,3)
        second = random.randint(1,3)

        return (first, second)

dice = Dice()
print(dice.roll())"""

"""
print("my name is\t\t\t emon das")
print("my name is emon das")"""

"""import random

class Dice:
    def roll(self):
 

        first = random.randint(1,6)
        second = random.randint(1,6)
        return (first, second)

dice = Dice()
print(dice.roll())"""

"""
from pathlib import Path

p = Path()

for file in p.glob("*.html"):
    print(file)"""

"""course = "Python for beginners"
print(len(course))
print(course.upper())
print(course.lower())
print(course.find("y"))
print(course.replace("for", "For"))

print("for" in course)"""

"""num = [5, 2, 4, 1, 8, 9, 2, 3]

max = num[0]

for number in num:
    if number < max:
        max = number
print(max)
"""

""""import math

print(math.floor(3))

print(abs(3))"""

"""
x = lambda a : a+ 3

print(x(5))"""

"""
secret_number = 2
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print("you Won!")
        break

    else:
        print("opps! Wrong")


else:
    print("Sorry! Try again")"""











help()







