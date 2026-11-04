# --- Task 1: Even or Odd ---
print("--- Task 1: Even or Odd ---")
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# --- Task 2: Exam Score ---
print("\n--- Task 2: Exam Grades ---")
score = int(input("Enter exam score (0-100): "))

# Check for invalid inputs first
if score < 0 or score > 100:
    print("Invalid score. Please enter a number between 0 and 100.")
elif score >= 80:
    print("A")
elif score >= 70:
    print("B")
elif score >= 60:
    print("C")
else:
    print("F")

# --- Task 3: Predicting If vs Elif ---
print("\n--- Task 3: If vs Elif ---")
x = 6 # Changed to 6 to prove the logic

print("Version 1 (Two ifs):")
if x > 5:
    print("A")
if x > 8:
    print("B")
else:
    print("C")

print("Version 2 (If / Elif):")
if x > 5:
    print("A")
elif x > 8:
    print("B")
else:
    print("C")

# --- Task 4: Age and Ticket (With parentheses fix) ---
print("\n--- Task 4: Entry Check ---")
age = int(input("Enter your age: "))
has_ticket = input("Do you have a ticket? (yes/no): ").lower()

# Parentheses group the two ticket options together. This ensures that 
# the "or" connects ONLY "yes" and "y", making it a single ticket check. 
# The age check then correctly applies to the result. Without the parentheses, 
# the "or" connects the entire age-and-ticket condition to the "y" check, 
# which bypasses the age requirement entirely.
if age >= 18 and (has_ticket == "yes" or has_ticket == "y"):
    print("Entry allowed.")
else:
    print("Entry denied.")