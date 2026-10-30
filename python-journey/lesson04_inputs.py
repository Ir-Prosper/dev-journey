# Ask for name and city
name = input("What is your name? ")
city = input("What is your city? ")
print(f"My name is {name} and I am from {city}.")

# Ask for age
age = input("What is your age? ")
print(type(age))

# Ask for two numbers (Version 1: No int())
num1 = input("Give the first number: ")
num2 = input("Give the second number: ")
print("The sum is:", num1 + num2)

# Fixed Version
num1 = int(input("Give the first number: "))
num2 = int(input("Give the second number: "))
print("The sum is:", num1 + num2)

