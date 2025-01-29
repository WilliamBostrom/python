# TIP CALCULATOR

print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tip = total_bill * (tip_percentage / 100)
total = total_bill + tip
each_person = total / people
each_person = round(each_person, 2)
print(f"Each person should pay: ${each_person}")




# # Subscripting
# print("hello"[-1])

# #string
# print("123" + "345")

# #integer
# print(123 + 345)


# #large integer
# print(123_456_789)

# #float
# print(3.14159)

# #boolean
# # print(len("hello") == 1)

# print(type(123) == int)


# num = int("123")
# print(num + int("345"))

# print("Number of letters in your name: " + str(len(input("What is your name? "))))


# print("my age: " + str(10))
# print(123 + 456)
# print(7 - 3)
# print(3 * 2)
# print(122 / 3)
# print(122 // 3)
# print(6**2)

# bmi = 100 / (2.00 ** 2)
# print(bmi)

# print(int(bmi))

# print(round(bmi, 2))

# print(6 + 4 / 2 - (1 * 2))


# name = input("What is your name? ")
# print("Hello " + name)
# print("Hello, " + name)

# age = 12
# print(f"Hello! You are {age} years old.")

# print("You are" + age + "years old.")