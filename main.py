import os
import random
from spaceship import print_fueldown, clear_terminal

print("Welcome to Astro Hangman Game")
print("* * * * * * * * * * * * * * * * ")

# word lists for different levels
wordlist_level1 = ['universe', 'galaxy', 'milkyway', 'planet', 'star', 'comet']
wordlist_level2 = ['astronaut', 'telescope', 'satellite', 'nebula', 'orbit', 'gravity']
wordlist_level3 = ['constellation', 'interstellar', 'microgravity',  'blackhole', 'exoplanet', 'quasar']

# maximum wrong guesses for different levels
max_wrongguesses_level1 = 6
max_wrongguesses_level2 = 5
max_wrongguesses_level3 = 4

# Clears the terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Choosing the level
def choose_level():
    while True:
        try:
            level = int(input("Which level would you like to play? Choose 1, 2, or 3: \n"))
            if level in [1, 2, 3]:
                return level
            else:
                print("Invalid input! Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input! Please enter a number (1, 2, or 3).")
level = choose_level() 

# Setting word list and max wrong guesses based on chosen level
if level == 1:
    wordlist = wordlist_level1
    max_wrongguesses = max_wrongguesses_level1
elif level == 2:
    wordlist = wordlist_level2
    max_wrongguesses = max_wrongguesses_level2
else:
    wordlist = wordlist_level3
    max_wrongguesses = max_wrongguesses_level3

##choose a random word from the list
randomword=random.choice(wordlist_level1)
print("\n" + "_ " * len(randomword))

def printword(guessedletters):
    counter=0 ##index position
    correct_letters=0
    for char in randomword:
        if(char in guessedletters):
            print(randomword[counter], end=" ")
            correct_letters +=1
        else:
            print("_", end=" ") 
        counter+=1
    return correct_letters    

amount_of_timeswrong=0
current_letters_guessed=[]
current_letters_right=0

while(amount_of_timeswrong != max_wrongguesses and current_letters_right != len(randomword)):
    print("\n Letters Guessed so far: ")
    for letter in current_letters_guessed:
        print(letter, end=" ")
    letterguessed=input("\n Guess a letter: \n").lower() ##convert input to lower
    ##check if the input is a valid alphabetical letter and the length of the letter
    if not letterguessed.isalpha() or len(letterguessed) !=1:
        print("Invalid input! Please enter an alphabetical letter.")
        continue
    if letterguessed in current_letters_guessed:
        print("You already guessed that letter!")
        continue
    current_letters_guessed.append(letterguessed)  

    ##when the user is right
    if letterguessed in randomword:
        print_fueldown(amount_of_timeswrong)
        current_letters_right =printword(current_letters_guessed)
    ##when the user is wrong
    else:
        amount_of_timeswrong+=1
        remaining_guesses=max_wrongguesses-amount_of_timeswrong
        print(f"Wrong guess!! You are allowed to make {remaining_guesses} more wrong guesses")   
        print_fueldown(max_wrongguesses - amount_of_timeswrong)
        printword(current_letters_guessed)

if current_letters_right == len(randomword):
    print("\nCongratulations! You guessed the word:", randomword)
else:
    print("\nGame is over! The word was:", randomword)
    print("Thank you for playing!")

    
            
         




