try:

    age = int((input("age: ")))
    income = 2000
    risk = income / age
    print(age)

except ZeroDivisionError:
    print("age cann't be zero")
except ValueError:
    print("Invalid Value")