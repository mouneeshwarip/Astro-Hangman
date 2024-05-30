import random
print("Welcome to Astro Hangman Game")
print("_ _ _ _ _ _ _")
wordlist_level1=['Universe','Galaxy','Milkyway']


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
    wrongletters=[]
    for char in randomword:
        if(char in guessedletters):
            print(randomword[counter], end=" ")
        else:
            print("_", end=" ") 
        counter+=1
    ##keeping track of wrongly guessed letters
    for guess in guessedletters:
        if guess not in randomword:
            wrongletters.append(guess)
    return wrongletters  

amount_of_timeswrong=0
len_of_wordstoguess=len(randomword)
current_guess_index=0
current_letters_guessed=[]
current_letters_right=0

while(amount_of_timeswrong != 6 and current_letters_right != len_of_wordstoguess):
    print("\n Letters Guessed so far: ")
    for letter in current_letters_guessed:
        print(letter, end=" ")
    letterguessed=input("\n Guess a letter: ")
    ##when the user is right
    if(randomword[current_guess_index] == letterguessed):
        print_fueldown(amount_of_timeswrong)
        current_guess_index+=1
        current_letters_guessed.append(letterguessed)  
        current_letters_right = printword(current_letters_guessed)
    ##when the user is wrong
    else:
        print("here one bar battery down") 
        amount_of_timeswrong+=1
        current_letters_guessed.append(letterguessed)   
        print_fueldown(amount_of_timeswrong)
        current_letters_right = printword(current_letters_guessed)

print("Game is over! Thank you for playing")


    
            
         




