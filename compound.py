money=0
years = 0
while years <= 10:
    depo = float(input("Deposit: "))
    money = depo+money
    sum=money*0.06
    money=sum+money
    years+=1
    print(money)