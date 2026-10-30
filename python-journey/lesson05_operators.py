# ==========================================
# LESSON 5: OPERATORS, LOGIC & TIME CONVERTER
# ==========================================

print("--- Part 1: Basic Operators ---")
x = 20
y = 6
print("x + y =", x + y)
print("x - y =", x - y)
print("x * y =", x * y)
print("x / y =", x / y)
print("x // y =", x // y)
print("x % y =", x % y)
print("x ** 2 =", x ** 2)
print("10 / 2 =", 10 / 2, "| Type:", type(10 / 2))

print("\n--- Part 2: The Sharper Test (Precedence & Negatives) ---")
print("-7 // 2 =", -7 // 2)
print("-7 % 2 =", -7 % 2)  # The trap: remainder takes the sign of the divisor
print("10 - 2 * 3 =", 10 - 2 * 3)
print("(10 - 2) * 3 =", (10 - 2) * 3)
print("2 ** 3 ** 2 =", 2 ** 3 ** 2) # The trap: ** goes right to left
print("7 // 2.0 =", 7 // 2.0)

print("\n--- Part 3: Modulo Pattern ---")
print("14 % 2 =", 14 % 2)
print("15 % 2 =", 15 % 2)

print("\n--- Part 4: Comparisons (Booleans) ---")
age = 34
print("age >= 18:", age >= 18)
print("age == 30:", age == 30)
print("age != 34:", age != 34)

# Note: print(5 = 5) would cause a SyntaxError, so we comment it out to let the script run.
# print(5 = 5) 

print("\n--- Part 5: Float Precision Teaser ---")
print("0.1 + 0.2 =", 0.1 + 0.2)

print("\n--- Part 6: Time Converter Challenge ---")
# This will pause and ask you to type a number in the terminal.
total_minutes = int(input("Enter total minutes: "))
hours = total_minutes // 60
minutes = total_minutes % 60
print(f"{total_minutes} minutes is {hours} hours and {minutes} minutes.")