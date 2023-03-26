numbers = [1,3,2,4,2,7,6,7,9,6]


# numbers2 = numbers.copy()
# numbers.insert(1,10)  // add new item where you want (1,10)(index, value)
# numbers.append(10) //add new item in list
# numbers.clear() //clear all the item
# numbers.remove(6) // we can romove the existing item
# print(numbers.index(7)) // print the index numbers of our list
# numbers.pop() // remove the last number in the list
# print(30 in numbers) // boolean  ......... True or False
# print(numbers.count(7)) // how many numbers we have in our list
# numbers.sort() // all the item are sortted in ascending order
# numbers.reverse() // all the item are sortted in descending order

print(numbers)


#   * write a program to remove the duplicates in a list *
num = [1,3,2,4,2,7,6,7,9,6]
uniq = []
for number in num:
    if number not in uniq:
        uniq.append(number)

print(uniq)


