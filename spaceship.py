import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_spaceship(wrong):
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'

    spaceship = """
     .'.
    |o o|
   _| = |_
  |       |
  |_______|
    """

    if wrong >= 5:
        print(GREEN + spaceship + RESET)
    elif wrong >= 3:
        print(YELLOW + spaceship + RESET)
    else:
        print(RED + spaceship + RESET)
   
        
    

'''def print_fueldown(wrong):
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
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
    '''    


'''def print_fueldown(wrong):
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'

    spaceship_full = f"""
       .'.
      |o o|
     _| = |_
    |       |
    |       |
    |_______|
    """

    spaceship = {
        6: GREEN + spaceship_full + RESET,
        5: GREEN + spaceship_full + RESET,
        4: YELLOW + spaceship_full + RESET,
        3: YELLOW + spaceship_full + RESET,
        2: RED + spaceship_full + RESET,
        1: RED + spaceship_full + RESET,
        0: RED + spaceship_full + RESET
    }

    print(spaceship[wrong])
    '''
