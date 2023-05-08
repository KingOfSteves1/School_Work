import statistics
numlist = []
print("How many number are you going to put into the list?")
ui = int(input())
while ui != 0:
    num =input("Number: ")
    numlist.append(int(num))
    ui-=1
print(numlist)
sum = 0
for i in numlist:
    sum +=i
sum = sum / len(numlist)
med = 0
n = len(numlist)
numlist.sort()
 
if n % 2 == 0:
    median1 = numlist[n//2]
    median2 = numlist[n//2 - 1]
    median = (median1 + median2)/2
else:
    median = numlist[n//2]
def mode1(lst):
    y={}
    for a in lst:
        if not a in y:
            y[a]=1
        else:
            y[a]+=1
    return [g for g,l in y.items() if l==max(y.values())]
print("Mode is: "+str(mode1(numlist)))
print("Median is: " + str(median))
print("Mean is: "+str(sum))
