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