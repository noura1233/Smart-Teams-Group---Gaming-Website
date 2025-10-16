import os
clear = lambda: os.system('cls') #Creates obj for clearing serial screen

#Variables
state = 0 #Controls what part of game
#0 - Title, 1 - Setup, 2 - Start, MORE TO BE ADDED, 9 - End
win = 21


while True:
    if(state==0):
        clear()
        print("TItle Screen")
        choice = input("Play? (y/n) > ")
        if(choice=="y"):
            state = 1
        elif(choice=="n"):
            state = 9



    if(state==9):
        print("Program end")
        break
