#Import for assignment and also making some things just easier
import random as r
import time as t
import os


#Assigning Variables
totalgang = 3500
wlevel = 200
ui = "sus among us"
food = 3500
wiocean = 0
money = 0
havenuke = False
years = 1
cofgang = r.randint(1500,3000)

#It begins...
def start():
    global totalgang
    global wlevel
    global ui
    global food
    global wiocean
    global money
    global havenuke
    global years
    global cofgang
    totalgang = 3500
    wlevel = 200
    ui = "sus among us"
    food = 3500
    wiocean = 0
    money = 0
    havenuke = False
    years = 1
    cofgang = r.randint(1500,3000)
    print("Welcome to totally ~~accurate Ganges River Dolphin Simulator!")
    t.sleep(1)
    sim()

#Choices, choices...
def sim():
    os.system('cls')
    global food
    food+=r.randint(500,1500)
    print("There are currently: "+str(totalgang) +" Ganges River Dolphins\nYou have $"+str(money)+"\nCurrent food: "+str(food)+"\nThere is currently "+str(wiocean)+" waste in the ocean!\nThe Water level is currently at "+str(wlevel)+"\nIt is currently year "+str(years)+"\nChoose 1 action:\nWater Level\t1\nBuy Food\t2\nDispose Waste\t3\nLaunch Nuke\t4\nArm Dolphins\t5\nSell Dolphins\t6\nBuy Dolphins\t7\nDo Nothing\t8")
    ui = input("")
    if ui == "1":
        waterlevel()
    elif ui == "2":
        givefood()
    elif ui == "3":
        disposewaste()
    elif ui == "4":
        nuke()
    elif ui == "5":
        arm()
    elif ui == "6":
        sell()
    elif ui == "7":
        buy()
    elif ui == "8":
        dolphcheck()
    elif ui == "0":
        cheat()
    else:
        print("You dumb")
        t.sleep(.3)
        os.system("cls")
        sim()

#To adjust waterlevel according to player        
def waterlevel():
    os.system('cls')
    print("The water level is currently at: "+str(wlevel)+"\nChoose one option:\nRaise Water Level\t1\nLower Water Level\t2")
    ui = input("")
    if ui == "1":
        wraise()
    elif ui == "2":
        wlower()
    else:
        print("You dumb")
        t.sleep(.3)
        os.system("cls")
        sim()

#what a nice person you are, raising the water level, hopefully you don't do bad things        
def wraise():
    global wlevel
    print("How much do you want to raise the water level by?")
    ui = input("")
    if int(ui) >= 1:
        wlevel = wlevel + int(ui)
        dolphcheck()
    else:
        print("You dumb")
        t.sleep(.3)
        os.system('cls')
        sim()

#You evil person        
def wlower():
    global wlevel
    print("How much do you want to lower the water level by?")
    ui = input("")
    if int(ui) >=1:
        wlevel = wlevel - int(ui)
        dolphcheck()
    else:
        print("You dumb")
        t.sleep(.3)
        os.system('cls')
        sim()

#Dolphin Burgers       
def givefood():
    global food
    global money
    print("How much food do you want to give them?\nFood currently cost $100.")
    ui = input("")
    if int(ui) >= 1 and money >int(ui)*100:
        food +=int(ui)
        money = money-int(ui)*100
        dolphcheck()
    else:
        print("You dumb")
        t.sleep(.3)
        os.system('cls')
        sim()

#I'm reporting you to Microsoft!!11!1        
def cheat():
    global money
    global years
    global totalgang
    global food
    global wiocean
    global wlevel
    print("Welcome you cheater!\nChoose one option\nSet Money\t1\nSet Year\t2\nSet Ganges\t3\nSet Food\t4\nSet Waste\t5\nSet Water\t6\nLeave Cheats\t7")
    ui = input("")
    if ui == "1":
        ui = input("Set Money: ")
        money = int(ui)
        cheat()
    elif ui == "2":
        ui=input("Set Year: ")
        years = int(ui)
        cheat()
    elif ui =="3":
        ui=input("Set Ganges River Dolphins: ")
        totalgang = int(ui)
        cheat()
    elif ui == "4":
        ui = input("Set Food: ")
        food = int(ui)
        cheat()
    elif ui =="5":
        ui = input("Set Waste: ")
        wiocean = int(ui)
        cheat()
    elif ui == "6":
        ui = input("Set Water Level: ")
        wlevel = int(ui)
        cheat()
    else:
        sim()

#You are not very nice >:(        
def disposewaste():
    global wiocean
    print("How much waste do you want to dispose of?")
    ui = input("")
    if int(ui) >= 1:
        wiocean+=int(ui)
        dolphcheck()
    else:
        print("You dumb")
        t.sleep(.3)
        os.system('cls')
        sim()

#Kablooey!        
def nuke():
    global money
    print("Nukes currently cost ~6 million\nBuy Nuke?\nY|N")
    ui = input("")
    if ui.lower() =="y" and money >=6000000:
        havenuke=True
        if havenuke==True:
            print("Do you want to launch the nuke?\nY|N")
            ui = input("")
            if ui.lower() == "y":
                extinction()
            else:
                dolphcheck()
    else:
        dolphcheck()

#What would happen if you gave dolphins .50 cals...        
def arm():
    global money
    global totalgang
    print("Gun currently cost $200/dolphin\nCurrent cost $"+str(totalgang*200)+"\nDo you want to buy a gun for each of your dolphins?\nY|N")
    ui = input("")
    if ui.lower() =="y" and money >totalgang*200:
        money = money-totalgang*200
        totalgang = totalgang*2
        dolphcheck()
    else:
        dolphcheck()

#The act of selling the dolphins to earn money to feed the others, is it kind? NO 
def sell():
    global totalgang
    global money
    c = r.randint(2,2000)
    print("How many Ganges River Dolphins do you want to sell?\nThey currently sell for $"+str(c))
    ui = input("")
    if int(ui)>=1:
        money=int(ui)*c+money
        totalgang -=int(ui)
        dolphcheck()
    else:
        print("You dumb")
        t.sleep(.3)
        os.system('cls')
        dolphcheck()

#Intergalactic space traders offering us these dolphins for a price, of course        
def buy():
    global totalgang
    global money
    print("Ganges River Dolphins currently cost "+str(cofgang)+"$\nHow much do you want to buy?")
    ui = input("")
    if int(ui)>=1:
        money = money-int(ui)*cofgang
        totalgang+=int(ui)
        dolphcheck()
    else:
        print("You dumb")
        t.sleep(.3)
        os.system('cls')
        sim()

#Very important as it basically 'ends year'        
def dolphcheck():
    global years
    global wiocean
    global wlevel
    global money
    global food
    global totalgang
    years+=1
    
    totalgang-=wiocean
    
    if food <0:
        food = 0
    elif food > totalgang:
        totalgang += r.randint(2,200)
    elif wlevel <= 100:
        totalgang -= r.randint(1, 10)
    elif food < totalgang:
        totalgang -= r.randint(1000, 3000)
    elif wlevel >600:
        totalgang += r.randint(20,50)
    elif money <0:
        print("Your Broke")
        totalgang = 0
        extinction()
    food = food-totalgang
    if totalgang <= 0:
        extinction()
    sim()

#Oh no! Anyways...    
def extinction():
    os.system('cls')
    print("...")
    t.sleep(1)
    os.system('cls')
    print("They're all gone")
    t.sleep(1)
    os.system("cls")
    print("CONGRATULATIONS!! YOU HAVE KILLED ALL THE GANGES RIVER DOLPHINS!!\nPress play again!")
    ui = input("Do you want to play again?\nY|N\n")
    if ui.lower() == "y":
        start()
    else:
        print("Ok")

#Time rolls back        
start()
