# Plan: 
# 1. Get total minutes from the user.
# 2. Calculate the total hours using floor division (// 60).
# 3. Calculate the remaining minutes using modulo (% 60).
# 4. Decide the word "hour" or "hours" using an if/else.
# 5. Decide the word "minute" or "minutes" using an if/else.
# 6. Print the final sentence on one line using an f-string.

print("--- Time Converter ---")
total_minutes = int(input("Enter total minutes: "))

hours = total_minutes // 60
minutes = total_minutes % 60

# Decide the words first
if hours == 1:
    hour_word = "hour"
else:
    hour_word = "hours"

if minutes == 1:
    minute_word = "minute"
else:
    minute_word = "minutes"

# Print it all on one line
print(f"{hours} {hour_word} and {minutes} {minute_word}")