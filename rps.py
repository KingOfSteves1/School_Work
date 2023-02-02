import random
import os
import time
pscore=0
bscore=0
clear = lambda: os.system('cls')
def losecheck():
    if bscore==3:
        if pscore<bscore:
            print("You Lost Permently!")
    else:
        game()
def wincheck():
    if pscore ==3:
        if bscore<pscore:
            print("You Won The Whole Game!")
    else:
        game()
def game():
    print("W")
    time.sleep(.1)
    clear()
    print("We")
    time.sleep(.1)
    clear()
    print("Wel")
    time.sleep(.1)
    clear()
    print("Welc")
    time.sleep(.1)
    clear()
    print("Welco")
    time.sleep(.1)
    clear()
    print("Welcom")
    time.sleep(.1)
    clear()
    print("Welcome")
    time.sleep(.1)
    clear()
    print("Welcome ")
    time.sleep(.1)
    clear()
    print("Welcome t")
    time.sleep(.1)
    clear()
    print("Welcome to")
    time.sleep(.1)
    clear()
    print("Welcome to ")
    time.sleep(.1)
    clear()
    print("Welcome to R")
    time.sleep(.1)
    clear()
    print("Welcome to Ro")
    time.sleep(.1)
    clear()
    print("Welcome to Roc")
    time.sleep(.1)
    clear()
    print("Welcome to Rock")
    time.sleep(.1)
    clear()
    print("Welcome to Rock P")
    time.sleep(.1)
    clear()
    print("Welcome to Rock Pa")
    time.sleep(.1)
    clear()
    print("Welcome to Rock Pap")
    time.sleep(.1)
    clear()
    print("Welcome to Rock Pape")
    time.sleep(.1)
    clear()
    print("Welcome to Rock Paper")
    time.sleep(.1)
    clear()
    print("Welcome to Rock Paper ")
    time.sleep(.1)
    clear()
    print("Welcome to Rock Paper S")
    time.sleep(.1)
    clear()
    print("Welcome to Rock Paper Sc")
    time.sleep(.1)
    clear()
    print("Welcome to Rock Paper Sci")
    time.sleep(.1)
    clear()
    print("Welcome to Rock Paper Scis")
    time.sleep(.1)
    clear()
    print("Welcome to Rock Paper Sciss")
    time.sleep(.1)
    clear()
    print("Welcome to Rock Paper Scisso")
    time.sleep(.1)
    clear()
    print("Welcome to Rock Paper Scissor")
    time.sleep(.1)
    clear()
    print("Welcome to Rock Paper Scissors")
    global pscore
    global bscore
    print("Your Score: "+str(pscore)+". CPU's Score: " +str(bscore))
    pinput = input("Choose Rock, Paper, Or Scissors: ")
    rps=["Rock", "Paper", "Scissors"]
    rpsa = random.choice(rps)
    print("Cpu chose "+ rpsa )
    time.sleep(1)
    
    if pinput.lower()=="rock":
        if rpsa == "Rock":
            print("Its a tie.")
            time.sleep(3)
            game()
        elif rpsa == "Paper":
            print("You Lost!")
            time.sleep(3)
            bscore+=1
            losecheck()
        elif rpsa == "Scissors":
            print("You won!")
            time.sleep(3)
            pscore+=1
            wincheck()
    elif pinput.lower()=="paper":
        if rpsa == "Rock":
            print("You won!")
            time.sleep(3)
            pscore+=1
            wincheck()
        elif rpsa == "Paper":
            print("Its a tie.")
            time.sleep(3)
            game()
        elif rpsa == "Scissors":
            print("You Lost!")
            time.sleep(3)
            bscore+=1
            losecheck()
    elif pinput.lower()=="scissors":
        if rpsa == "Rock":
            print("You Lost!")
            time.sleep(3)
            bscore+=1
            losecheck()
        elif rpsa == "Paper":
            print("You won!")
            time.sleep(3)
            pscore+=1
            wincheck()
        elif rpsa == "Scissors":
            print("Its a tie.")
            time.sleep(3)
            game()
game()