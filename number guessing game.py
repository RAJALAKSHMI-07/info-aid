import random

# Set the range 
lower_limit = 1
upper_limit = 50
secret_number = random.randint(lower_limit, upper_limit)

attempts = 0
max_attempts = 10

print("Welcome to the Number Guessing Game! Guess a number between", lower_limit, "and", upper_limit, ". You have", max_attempts, "attempts.")

while attempts < max_attempts:
    try:
        guess = int(input("Enter your guess: "))
        
        if guess < lower_limit or guess > upper_limit:
            print("Please enter a number between", lower_limit, "and", upper_limit, ".")
            continue
        
        if guess == secret_number:
            print("Congratulations! You guessed the correct number, which is", secret_number, ".")
            break
        elif guess < secret_number:
            print("Try a higher number.")
        else:
            print("Try a lower number.")
        
        attempts += 1
        remaining_attempts = max_attempts - attempts
        print("You have", remaining_attempts, "attempts remaining.")
    
        # Provide hints
        if remaining_attempts > 0:
            if secret_number % 2 == 0:
                print("Hint: The secret number is even.")
            else:
                print("Hint: The secret number is odd.")
            
            if secret_number > 25:
                print("Hint: The secret number is greater than 25.")
            else:
                print("Hint: The secret number is less than or equal to 25.")
    
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if attempts == max_attempts:
    print("Sorry, you've run out of attempts. The number was", secret_number, ".")
