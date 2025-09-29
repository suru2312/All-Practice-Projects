import os
import random
from celebs_data import data
from art import logo, vs

def format_data(account):
    """Formats the account data into printable format."""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}."

def check_answer(user_guess, a_followers, b_followers):
    """Takes the user guess and check the followers count between account A and B."""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A : {format_data(account_a)}")
    print(vs)
    print(f"Against B : {format_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B' : ").lower()
    os.system("cls")

    a_follower_count = account_a["followers_count"]
    b_follower_count = account_b['followers_count']
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You're Right! Current Score : {score}.")
        print(logo)
    else:
        print(f"Sorry, that's wrong. Final Score : {score}.")
        game_should_continue = False