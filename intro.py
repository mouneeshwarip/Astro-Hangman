import colorama
from colorama import Fore, Style

def display_logo():
    logo = f"""
{Fore.CYAN}
__        __   _                            _          _   _             
\\ \\      / /__| | ___ ___  _ __ ___   ___  | |_ ___   | | | | __ _ _ __  
 \\ \\ /\\ / / _ \\ |/ __/ _ \\| '_ ` _ \\ / _ \\ | __/ _ \\  | |_| |/ _` | '_ \\ 
  \\ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) | |  _  | (_| | | | |
   \\_/\\_/ \\___|_|\\___\\___/|_| |_| |_|\\___|  \\__\\___/  |_| |_|\\__,_|_| |_|
{Style.RESET_ALL}
"""
    print(logo)
# function to display rules
def display_rules():
    rules = f"""
{Fore.YELLOW}Welcome to Astro Hangman Game!{Style.RESET_ALL}
{Fore.GREEN}
Rules:
1. Choose a difficulty level: 1, 2, or 3.
2. You will be given a word related to space.
3. Guess the word one letter at a time.
4. You can make a limited number of wrong guesses based on the chosen level.
5. The spaceship's battery level will indicate your remaining guesses.
6. Guess the word before you run out of guesses to win the game!
{Style.RESET_ALL}
"""
    print(rules)