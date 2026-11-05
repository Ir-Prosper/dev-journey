#Guess 1: If I guess "python" on the first try, it should print 
# "Correct! It took you 1 attempt."
#Guess 2: If I guess "java", "c++", "python", it should print 
# "Wrong!", "Wrong!", "Correct! It took you 3 attempts."
#Guess 3: If I guess "java", "c++", "html", the game should 
# stop and print "Game over! You had 3 wrong guesses."

# PLAN: 
# I will use a while loop because the number of attempts is unknown.
# I will use 'break' to exit the loop early if the user guesses correctly,
# and to stop the loop if they hit 3 wrong guesses.

secret_password = "python"
attempts = 0
max_attempts = 3

print("--- Password Guess Game ---")

while attempts < max_attempts:
    guess = input("Enter your guess: ")
    attempts = attempts + 1  # Increase the attempt count
    
    if guess == secret_password:
        print(f"Correct! It took you {attempts} attempt(s).")
        break  # Exit the loop immediately because they won
    else:
        print("Wrong!")
        if attempts == max_attempts:
            print(f"Game over! You reached the maximum of {max_attempts} wrong guesses.")