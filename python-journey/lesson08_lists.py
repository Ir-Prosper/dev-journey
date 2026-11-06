# ==========================================
# LESSON 8: LISTS
# ==========================================

# --- Task 1: List Basics ---
# Prediction: 
# First will be 85.
# Last will be 92.
# Length will be 5.

marks = [85, 90, 78, 88, 92]

print("--- Task 1: List Basics ---")
print(f"First mark: {marks[0]}")
print(f"Last mark: {marks[-1]}")
print(f"Length: {len(marks)}")


# --- Task 2: The Index Error ---
# Prediction: 
# I expect marks[5] to crash the program because the list only has 5 items. 
# Python starts counting at 0, so the valid indexes are 0, 1, 2, 3, and 4. 
# Index 5 does not exist.

#print("\n--- Task 2: The Index Error ---")
#print(marks[5])


# --- Task 3: Loop through Marks ---
# Prediction: 
# It will print 85, 90, 78, 88, and 92 on separate lines.

print("\n--- Task 3: Loop through Marks ---")
for mark in marks:
    print(mark)


# --- Task 4: Append and Remove ---
# Prediction: 
# After append, 100 will be at the end.
# After remove, 78 will be gone. The list will be [85, 90, 88, 92, 100].

print("\n--- Task 4: Append and Remove ---")
marks.append(100)
print("After append(100):", marks)

marks.remove(78)
print("After remove(78):", marks)


# --- Task 5: Total and Average ---
# Prediction: 
# The variable that starts at 0 will be the 'total'.
# total should be 455, and average should be 91.0.
# The loop answers will agree with sum() and len().

print("\n--- Task 5: Total and Average ---")
total = 0
for mark in marks:
    total = total + mark

average = total / len(marks)

print(f"Total (using loop): {total}")
print(f"Average (using loop): {average}")
print(f"Total (using sum()): {sum(marks)}")
print(f"Average (using len()): {sum(marks) / len(marks)}")


# --- Task 6: Finding the Highest Mark ---
# Prediction: 
# I will start with 'highest = marks[0]' (which is 85).
# I will loop through each mark. If the mark is higher than the current 'highest', 
# I change 'highest' to equal that new mark. 
# It should find 100.

print("\n--- Task 6: Finding the Highest Mark ---")
highest = marks[0] # Start with the first mark

for mark in marks:
    if mark > highest:
        highest = mark

print(f"Highest mark (using loop): {highest}")
print(f"Highest mark (using max()): {max(marks)}")