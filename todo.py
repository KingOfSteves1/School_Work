# Imports for random
import random as r
import time as t
import os as o
#define critical vars
todo = ["Your text here", "Your text here"]
num = 1
#main core for todo list
def do():
    o.system('cls')
    global num, todo
    print("This is your to do list:")
    num = 1
    for i in todo:
        print(str(num)+": "+i)
        num+=1
    num =1
    print("Choose one thing to do.\nChange\t1\nAdd\t2\nRemove\t3")
    ui=input("")
    if ui == "1":
        change()
    elif ui =="2":
        add()
    elif ui =="3":
        remove()
    else:
        do()
#function to change to do listr
def change():
    global todo, num
    o.system('cls')
    print("This is your to do list:")
    for i in todo:
        print(str(num)+": "+i)
        num+=1
    print("What line do you want to change?")
    ui = input("")
    todo[int(ui)-1] = input("What do you want it to be?")
    do()
#function to add to do list
def add():
    global todo, num
    o.system('cls')
    print("What would you like to add?")
    ui = input()
    todo.append(ui)
    do()
#function to remove to do list
def remove():
    global todo, num
    print("Which item would you like to remove?")
    ui=input()
    print("Type the exact text to confirm: ")
    ui = input()
    todo.remove(ui)
    do()
#Boot main core
do()
