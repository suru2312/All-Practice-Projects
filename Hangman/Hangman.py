
import random
from Hangman_Art import HANGMANPICS, logo
from Hangman_Words import list_of_words


print()
print("=====Welcome to the Hangman Game=====")
print(logo)

random_word = [i for i in random.choice(list_of_words)]
real_random_word = ""
for i in random_word:
    real_random_word += i
lives = 6
placeholder = ""
for i in range(len(random_word)):
    placeholder += "_ "
print("You have to Guess this word :",placeholder)

game_over = False
correct_letters = set()

while not game_over:
    
    print(f"******************** {lives} / 6 LIVES LEFT ********************")
    guess = input("Guess a letter : ").lower()
    
    if guess in correct_letters:
        print(f"You have already guessed the letter : {guess}")
        
    display = ""
    
    for i in random_word:
        if guess == i:
            display += i + " "
            correct_letters.add(i)
        elif i in correct_letters:
            display += i + " "
        else:
            display += "_ "
            
    print()
    
    print(display)
    
    if guess not in random_word:
        lives -= 1
        print(f"You Guessed letter '{guess}, that's not in the word. You LOSE a life.'")
        print(f"You have {lives} lives remaining.")
        if lives == 0:
            game_over = True
            print(f"******************** IT WAS '{real_random_word}' ! YOU LOSE ********************")
    
    if "_ " not in display:
        print("******************** You Win! ********************")
        game_over = True
    
    print(HANGMANPICS[lives])