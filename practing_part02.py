"""number =[1,2,2,3,5,9,4,8,4,5,6]
uni = []
for num in number:
    if num not in uni:
        uni.append(num)
print(uni)"""


"""
num = [5,2,4,10,5,6,7]

uni = []

for item in num:
    if item not in uni:
        uni.append(item)
print(uni)"""

"""customer = {
    "name":"Emon das",
    "age":21,
    "phone":"018761464",
    "is_verified" : True
}
print(customer["name"])
print(customer.get("age"))
print(customer.get("is_verified"))
"""


"""Phone = input("> ")
digits = {
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "six",
    "7" : "seven",
    "8" : "eight",
    "9" : "nine",
}
output = " "
for item in Phone:
   output += digits.get(item, item) + " "
print(output)"""


"""message = input("> ")

x = message.split(" ")

emoji = {
    ":)" : "☺",
    ":(" : "☹"
}
output = " "
for item in x:
    output += emoji.get(item, item) + " "
print(output)
"""

"""
def math(x, y):
    return x * y
print(math(3,6))
"""

"""
def user(first_name, last_name):
    print(f"Hi! {first_name} {last_name}")

user("emon", "das")"""

"""
try:
    age=int(input("age:"))
    print(x)
except ValueError:
    print("age should be integer")
except NameError:
    print("x is not defined")"""





"""customer = {
    "name" : "emon das",
    "phone" : 2457641,
    "address" : "jamalkhan askar digir par chittagong"

}
customer["phone"] = 366652
print(customer["address"])
print(customer.get("name"))
print(customer.get("birth","nov 16 2000"))
print(customer["phone"])
"""


"""
number =[1,2,5,6,8,7,9]
max = number[0]

for max_num in number:
    if max_num > max:
        max = max_num

print(max)
"""

"""
phone = input("phone: ")
digits = {
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "six",
    "7" : "seven",
    "8" : "eight",
}
output = " "
for num in phone:
    output += digits.get(num, "!") + " "
print(output)
"""

"""
message = input("> ")
words = message.split(" ")

emoji = {
    ":)": "☺",
    ":(": "☹"
}
output = ""
for word in words:
  output += emoji.get(word, word) + " "
print(output)
"""


"""def user(firstname, lastname):
    print(f"{firstname} {lastname}")


user(lastname="emon", firstname="das")"""













