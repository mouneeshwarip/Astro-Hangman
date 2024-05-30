import random
print("**********")
print("Welcome to Astro Hangman Game")
wordlist_level1=['Universe','Galaxy','Milkyway']
input=input("Enter your guess: ")

##choose a random word from the list
randomword=random.choice(wordlist_level1)

for x in randomword:
    print("*", end=" ")

def fuel_down(wrong):
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
    wrongletters=0
    for char in randomword:
        if(char in guessedletters):
            print(randomword[counter], end=" ")
        else:
            print("*", end=" ") 
        counter+=1
    ##keeping track of wrongly guessed letters
    for guess in guessedletters:
        if guess not in randomword:
            wrongletters.append(guess)
    return wrongletters            
         




