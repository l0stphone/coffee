import time
import os
import sys

def clear():
    if(os.name == 'nt'):
        os.system('title Coffee')
        os.system('cls')
    elif(os.name == 'posix'):
        os.system('clear')
    else:
        print("Your Operating System is not supported by this version the game. Please try again or check the releases on GitHub or itch.")
        time.sleep(9)
        raise SystemExit

clear()
