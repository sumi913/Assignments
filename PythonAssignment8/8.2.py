# Write a txt file which has a word in each line like:
# Hands
# Legs
# India
# Crow
# Rain
# ...
#
# Write a python code to read the file and store the words in the list
#
# Write a function to guess a word randomly from the list.
#
# Now, write a function which asks user to guess the chosen word letter by letter.
# Show "incorrect" message to the wrong guessed letter.
# Display  letters in the clue word that were guessed correctly.
#
# Let say word is EVAPORATE
#
# >>> Welcome to Hangman!
# _ _ _ _ _ _ _ _ _
# >>> Guess your letter: S
# Incorrect!
# You left with 5 chances to guess.
#
# >>> Guess your letter: E
# E _ _ _ _ _ _ _ E
# ...
# And so on.
#
#
# 1)Only let the user guess 6 times, and tell the user how many guesses they have left.
# Keep track of the letters the user guessed.
# 2) If the user guesses a letter they already guessed, don’t penalize them - let them guess again.
# 3)When the player wins or loses, let them start a new game.

import random
def extract_file():
    with open('words.txt', 'r') as file:
        list=[]
        for line in file:
            for words in line.split():
                list.append(words)
    return list
def select_randomly():
    list=extract_file()
    word = random.choice(list)
    return word
def game():
    word=select_randomly()
    print("Guess the characters")
    guesses = ''
    turns = 6
    while turns > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print(char, end=" ")
            else:
                print("_")
                failed += 1
        if failed == 0:
            print("You Win")
            print("The word is: ", word)
            break
        guess = input("guess a character:")
        guesses += guess
        if guess not in word:
            turns -= 1
            print("Wrong")
            print("You have", + turns, 'more guesses')
            if turns == 0:
                print("You Loose")
game()