print("Welcome to cashier system : Enter 0 when finished enter the price in ech item")
totalPrice = 0
# Input amount of Item
countitem = 1

Howmuch = int(input("Enter price of the item" + str(countitem) + ':'))
while (Howmuch != 0):
    if (countitem == 5):
        print()
        print("Get the 5th item for free!")
        print()
    else:
        totalPrice = totalPrice+Howmuch
    countitem = countitem+1
    Howmuch = int(input("Enter price of the item" + str(countitem) + ':'))

print()
print("This is the total price : ", totalPrice)
# ตัวแปร isMember
print()
isMember = input("Member (Y/N) : ")

# เงื่อนไข Member
if (isMember == 'Y' or isMember == 'y'):
    print("Membership Discount : 10% off")
    totalPrice = totalPrice*0.9
else:
    print("Not a member")
print()
# RewardPoint
if (totalPrice >= 500) and (totalPrice < 1000):
    rewardPoint = ("Price above 500 : receive 50 reward points")
elif (totalPrice >= 1000) and (totalPrice < 5000):
    rewardPoint = ("Price above 1000 : receive 100 reward points")
elif (totalPrice >= 5000):
    rewardPoint = ("Price above 5000 : receive 500 reward points")
else:
    rewardPoint = ("Receive 0 point")

# Day
Day = input("What day is today : ")
if (Day == 'Saturday'):
    print("Saturday Discount 20% off")
    totalPrice = totalPrice*0.8
elif (Day == 'Sunday'):
    print("Sunday Discount 40% off")
    totalPrice = totalPrice*0.6
elif (Day == 'Monday') or (Day == 'Wednesday'):
    print("Monday and Wednesday special discount 30% off")
    totalPrice = totalPrice*0.7
else:
    print("No promotion")

# print price
print()
print("Please pay", round(totalPrice, 2), "Baht")
print(rewardPoint)
print("Thank you")
