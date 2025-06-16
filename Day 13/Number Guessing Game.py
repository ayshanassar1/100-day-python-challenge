import random

def number_guessing_game():
    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100...")
    
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("👉 Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("📉 Too low! Try again.")
            elif guess > secret_number:
                print("📈 Too high! Try again.")
            else:
                print(f"🎉 Correct! The number was {secret_number}.")
                print(f"✅ You guessed it in {attempts} attempts!")
                break
        except ValueError:
            print("❌ Please enter a valid number.")

# Start the game
number_guessing_game()
"""
Output:
🎯 Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100...
👉 Enter your guess: 50
📈 Too high! Try again.
👉 Enter your guess: 25
📉 Too low! Try again.
👉 Enter your guess: 37
🎉 Correct! The number was 37.
✅ You guessed it in 3 attempts!
"""
