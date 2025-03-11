import random
from hangman_words import word_list

possible_words = word_list
chosen_word = random.choice(possible_words)

print(chosen_word)

lives = 6
game_over = False

placeholder = "" 

for i in range(len(chosen_word)):
    placeholder += "_"

print(placeholder)

correct_letters = []

while game_over == False:
    display = ""
    guess = str(input("Guess a letter: ")).lower()

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else: 
            display += "_"

    print("Errors:", lives)
    print(display)

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            game_over_message = "You Lost!"

    if "_" not in display:
        game_over = True
        game_over_message = "You Won!!"

print(game_over_message)
