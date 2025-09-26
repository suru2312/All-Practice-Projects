import random
import os

logo = """
  _  _            _                ___                _              ___                
 | \| |_  _ _ __ | |__  ___ _ _   / __|_  _ ___ _____(_)_ _  __ _   / __|__ _ _ __  ___ 
 | .` | || | '  \| '_ \/ -_) '_| | (_ | || / -_|_-<_-< | ' \/ _` | | (_ / _` | '  \/ -_)
 |_|\_|\_,_|_|_|_|_.__/\___|_|    \___|\_,_\___/__/__/_|_||_\__, |  \___\__,_|_|_|_\___|
                                                            |___/                       
"""

# Function to choose difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard'. If you want to exit enter '0' : ")
    if level == "easy":
        return 10
    elif level == "hard":
        return 5
    elif level == "0":
        return 0
    else:
        return -1

# Function to check the guess
def check_answer(guess, answer):
    if guess == answer:
        print(f"✅ You got it! The number was {answer}.")
        return True
    elif guess > answer:
        print("📉 Too high.")
    else:
        print("📈 Too low.")
    return False

# Function to play the game
def play_game():
    os.system("cls")  # clear screen
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)

    attempts = set_difficulty()

    if attempts == 0:   # Exit
        print("Goodbye!")
        os.system("cls")
        return False
    elif attempts == -1:  # Wrong input
        os.system("cls")
        print("⚠️ Wrong Input! Try again.")
        return True

    guess = 0
    while attempts > 0 and guess != answer:
        print(f"\n❤️ Attempts left: {'♥' * attempts}")
        guess = int(input("Make a guess: "))
        
        if check_answer(guess, answer):
            break
        
        attempts -= 1
        if attempts == 0:
            print(f"💀 Game Over! The number was {answer}")
    return True

# Main loop
while True:
    if not play_game():
        break
    again = input("\nDo you want to play again? (y/n): ").lower()
    if again == "n":
        print("👋 Thanks for playing!")
        os.system("cls")
        break
