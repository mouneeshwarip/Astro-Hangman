import os
import random
print("Welcome to Astro Hangman Game")
print("* * * * * * * * * * * * * * * * ")
wordlist_level1=['universe','galaxy','milkyway']

##Clears the terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

##choose a random word from the list
randomword=random.choice(wordlist_level1)

for x in randomword:
    print("_", end=" ")

def print_fueldown(wrong):
    if(wrong==0):
        print("fuel full with green")
    elif(wrong==1):
        print("fuel one point down with g")
    elif(wrong==2):
        print("fuel two points down with g")   
    elif(wrong==3):
        print("fuel three points down with yell")   
    elif(wrong==4):
        print("fuel four points down with y")   
    elif(wrong==5):
        print("fuel five points down with red")   
    elif(wrong==1):
        print("fuel six points down with r") 

def printword(guessedletters):
    counter=0 ##index position
    for char in randomword:
        if(char in guessedletters):
            print(randomword[counter], end=" ")
        else:
            print("_", end=" ") 
        counter+=1

max_wrongguesses=6
amount_of_timeswrong=0
len_of_wordstoguess=len(randomword)
current_guess_index=0
current_letters_guessed=[]
current_letters_right=0

while(amount_of_timeswrong != 6 and current_letters_right != len_of_wordstoguess):
    print("\n Letters Guessed so far: ")
    for letter in current_letters_guessed:
        print(letter, end=" ")
    letterguessed=input("\n Guess a letter: ").lower() ##convert input to lower
    ##check if the input is a valid alphabetical letter and the length of the letter
    if not letterguessed.isalpha() or len(letterguessed) !=1:
        print("Invalid input! Please enter an alphabetical letter.")
        continue
    ##when the user is right
    if(randomword[current_guess_index] == letterguessed):
        print_fueldown(amount_of_timeswrong)
        current_guess_index+=1
        current_letters_guessed.append(letterguessed)  
        current_letters_right = printword(current_letters_guessed)
    ##when the user is wrong
    else:
        amount_of_timeswrong+=1
        current_letters_guessed.append(letterguessed) 
        remaining_guesses=max_wrongguesses-amount_of_timeswrong
        print(f"Wrong guess!! You are allowed to make {remaining_guesses} more wrong guesses")   
        print_fueldown(amount_of_timeswrong)
        current_letters_right = printword(current_letters_guessed)

print("\n Game is over! Thank you for playing")
print()


    
            
         




