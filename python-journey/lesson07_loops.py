# 1. Print the numbers 1 to 5 with a while loop.

# Prediction before running: I expect to see "Round: 1" up to "Round: 5".
# The loop will stop when count becomes 6.

count = 1
while count <= 5:
    print(f"Round: {count}")
    count = count + 1
    
# 2. Print the numbers 1 to 5 with a for loop and range.

# Prediction before running: I expect to see 1, 2, 3, 4, 5 printed on separate lines.
# The start value is 1. The stop value must be 6 (because range stops before the last number).
# So range(1, 6) will include 5.

for i in range(1, 6):
    print(f"i is: {i}")
    
# 3. Predict: what do range(1, 4) and range(0, 10, 2) print? Check with list(range(...)).

# range(1, 4) will print: [1, 2, 3]
# range(0, 10, 2) will print: [0, 2, 4, 6, 8]
# range(start, stop): It starts at 1 and goes up to, but does not include, 4. 
# So it generates 1, 2, 3.
# range(start, stop, step): It starts at 0, goes up to (but doesn't include) 10, 
# and takes steps of 2. So it generates 0, 2, 4, 6, 8.

print(list(range(1, 4)))
print(list(range(0, 10, 2)))

# 4. Print the 5 times table (5 x 1 = 5 up to 5 x 10 = 50) with a loop. Use an f-string.

# range(1, 11) creates a sequence of numbers from 1 up to 10 
# (Python stops right before the second number, so 11 is not included).
# The loop variable i takes on each of those numbers one by one.
# The f-string (f"...") allows us to embed the variables i and 5 * i directly inside the text 
# using curly braces {}.
# Prediction before running: I expect to see exactly 10 lines of output, 
# starting with "5 x 1 = 5" and ending with "5 x 10 = 50".

for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")
    
# Find the bug: write a while loop that forgets to change the variable.
# Run it, stop it with Ctrl+C, and tell me what you saw and why it happened.

#count = 1
#while count <= 5:
 #   print("Stuck in the loop!")
    # BUG: We forgot to write count = count + 1 here!
    
# 6. What variable will hold the total? I will name it total.
# What value does it start with? It must start at 0.
# Why? If I start it at 1, the sum will be wrong because I will accidentally count the number 1 twice.
# Starting at 0 ensures I can safely add every number from 1 to n to it without changing the initial value.
#If the user types 0: The sum will be 0. The loop will be range(1, 1). 
# Since the start and stop are the same, the loop will not run at all, 
# leaving total at its starting value of 0.
#If the user types -3: The sum will be 0. The loop will be range(1, -2). 
# Because the start (1) is greater than the stop (-2) and there is no negative step provided,
# Python's range() will generate an empty sequence. The loop body will not execute, 
# and total will remain 0.


n = int(input("Enter a number n: "))

if n < 1:
    print("Invalid input. Please enter a positive integer (1 or higher).")
else:
    total = 0
    for i in range(1, n + 1):
        total = total + i
    print(f"The sum of all numbers from 1 to {n} is: {total}")
