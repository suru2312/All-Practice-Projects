
import random

HANGMANPICS = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
      |
      |
      |
      |
========='''    
]

print()
print("=====Welcome to the Hangman Game=====")
print()

list_of_words = ["apple", "river", "mountain", "cloud", "guitar", "python", "forest", "dream", "ocean", "flame",
                "castle", "shadow", "flower", "storm", "mirror", "stone", "sky", "tree", "fire", "light",
                "dragon", "whisper", "sand", "moon", "star", "book", "bridge", "wind", "magic", "song",
                "path", "heart", "wolf", "island", "gold", "sword", "king", "queen", "rain", "sun"]

random_word = [i for i in random.choice(list_of_words)]
lives = 6
placeholder = ""
for i in range(len(random_word)):
    placeholder += "_ "
print("Total Lives :", lives)
print("You have to Guess this word :",placeholder)

game_over = False
correct_letters = set()

while not game_over:
    guess = input("Guess a letter : ").lower()
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
        print()
        print(f"You have {lives} lives remaining.")
        if lives == 0:
            print("Game Over")
            game_over = True
    
    if "_ " not in display:
        print("You Win!")
        game_over = True
    
    print(HANGMANPICS[lives])