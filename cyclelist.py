import random as r
import time as t
nums = ["AS","2S","3S","4S","5S","6S","7S","8S","9S","10S","JS","QS","KS","AC","2C","3C","4C","5C","6C","7C","8C","9C","10C","JC","QC","KC","AD","2D","3D","4D","5D","6D","7D","8D","9D","10D","JD","QD","KD","AH","2H","3H","4H","5H","6H","7H","8H","9H","10H","JH","QH","KH",]
r.shuffle(nums)
ui = input("Pick a card. Make sure its in caps! Ex AS(Ace of spades), 5C (5 of clubs)\n")
gotcard =False
rnum=0
while gotcard!=True:
    print(nums[rnum])
    if ui == nums[rnum]:
        print("Here is your card! "+ui)
        gotcard=True
    t.sleep(.5)
    rnum+=1