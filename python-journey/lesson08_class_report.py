# PLAN:
# I will use a 'while' loop to get the input because I need exactly 5 VALID marks.
# I will use a 'for' loop to generate the report.
# Input() gives text. Before converting to float, I will use .replace().isdigit() 
# to check if the user typed letters. If they did, I use 'continue'.
# If the number is out of the 0-100 range, I also use 'continue'.

marks = []
count = 0

print("--- Enter 5 Marks (0-100) ---")
while count < 5:
    mark_input = input(f"Enter mark {count + 1}: ")
    
    # Check if the input is actually a number (allows one decimal point)
    if not mark_input.replace('.', '', 1).isdigit():
        print("Invalid input. Please enter numbers only between 0 and 100. Try again.")
        continue  # Skips the rest of the loop and asks again
        
    mark = float(mark_input)
    
    # Check if the number is between 0 and 100
    if mark < 0 or mark > 100:
        print("Invalid mark. Must be between 0 and 100. Try again.")
        continue  # Skips adding it, asks again
        
    marks.append(mark)
    count += 1  # Only increases if the mark is fully valid

# --- Generate Report ---
total = 0
highest = marks[0]
lowest = marks[0]
pass_count = 0

for mark in marks:
    total += mark
    if mark > highest:
        highest = mark
    if mark < lowest:
        lowest = mark
    if mark >= 50:
        pass_count += 1

average = total / len(marks)

print("\n--- CLASS REPORT ---")
print(f"All marks: {marks}")
print(f"Total: {total}")
print(f"Average: {average:.2f}")
print(f"Highest mark: {highest}")
print(f"Lowest mark: {lowest}")
print(f"Passed (>= 50): {pass_count} out of {len(marks)}")