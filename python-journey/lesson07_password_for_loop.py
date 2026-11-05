# PLAN:
# Both while and for loops work here. The only unknown is whether the user 
# wins early. I am using a for loop with range(max_attempts) because 
# the maximum number of guesses is fixed and known.
# The for...else block helps us know if the user lost (else runs if no break).

secret_password = "python"
max_attempts = 3

print("--- Password Guess Game (For Loop) ---")

for attempt in range(max_attempts):
    guess = input("Enter your guess: ").strip().lower()
    
    if guess == secret_password:
        print(f"Correct! It took you {attempt + 1} attempt(s).")
        break
else:
    print(f"Game over! You reached the maximum of {max_attempts} wrong guesses.")