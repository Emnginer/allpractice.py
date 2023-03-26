"""customer = {
    "name" : "Emon das",
    "age" : 21,
    "phone" : "0187164"
}
customer["birthdate"] = "jan 4 2000"

print(customer["birthdate"])
"""



phone = input("phone: ")

digit_mapping = {
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "six",
    "7" : "seven",
    "8" : "eight" ,
    "9" : "nine",
    "0" : "zero"

}
output = ""
for ch in phone:
  output += digit_mapping.get(ch, "!") + " "
print(output)