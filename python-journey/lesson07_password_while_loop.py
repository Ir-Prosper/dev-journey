# PLAN: 
# Both while and for loops work here. The only unknown is whether the user 
# wins early. I am using a while loop here as a design choice.
# The loop condition (attempts < max_attempts) will stop the game 
# automatically after 3 wrong guesses.
# I will use 'break' to exit the loop early when the user guesses correctly.

secret_password = "python"
attempts = 0
max_attempts = 3

print("--- Password Guess Game ---")

while attempts < max_attempts:
    # .strip() removes spaces at the beginning/end, .lower() makes it lowercase
    guess = input("Enter your guess: ").strip().lower()
    attempts += 1  # Increase the attempt count
    
    if guess == secret_password:
        print(f"Correct! It took you {attempts} attempt(s).")
        break  # Exit the loop immediately because they won
    else:
        print("Wrong!")
        if attempts == max_attempts:
            # I updated this text to match exactly what the program prints below
            print(f"Game over! You reached the maximum of {max_attempts} wrong guesses.")