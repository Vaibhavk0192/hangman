import random
from art import stages, logo
from words import word_list
import os 
clear=lambda:os.system('cls')

print(logo)
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
games_lives = 6
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    print(display)
    guess = input("\nGuess a Letter: ").lower()
    clear()

    for position in range(word_length):
        if chosen_word[position] == guess:
            display[position] = guess
    if guess not in chosen_word:
        games_lives -= 1
        if games_lives == 0:
            end_of_game = True
            print("You Loose")
            print(f"The Chosen Word is {chosen_word}\n")
    print(stages[games_lives])
    if "_" not in display:
        end_of_game=True
        print("You Win")
