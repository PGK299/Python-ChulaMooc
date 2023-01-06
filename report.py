###  Project  ###
existingReport = [1500, 2000, 3000, 4000, 5000, 1000, 2000, 500, 3000,
                  1000, 2000, 1500, 1000, 2000, 1000, 500, 1400, 2000, 3000, 5000, 1000]
weekDay = ['Monday', 'Tuesday', 'Wednesday',
           'Thusday', 'Friday', 'Saturday', 'Sunday']
week4 = []
countDay = 0
totalMoney = 0

print("Welcome to Sales report")
print("Enter daily sales (Baht)")
print()

while (countDay < 7):
    moneyDay = int(input("Daily sales Amount (Baht) " +
                   '---> ' + weekDay[countDay] + ' : '))
    countDay = countDay+1
    week4.append(moneyDay)

monthlyReport = existingReport+week4
print()
print("The total sales of this month is : ", sum(monthlyReport))
print("The average of sale is : ", round(
    sum(monthlyReport)/len(monthlyReport), 2))


InfoWeekReport = int(
    input("What week do you want to see (1-4) Press 0 fpr exit : "))
while (InfoWeekReport != 0):
    print()
    if (1 <= InfoWeekReport <= 4):
        print(monthlyReport[(InfoWeekReport-1)*7:InfoWeekReport*7])
        print("Total sales of this week is : ", sum(
            monthlyReport[(InfoWeekReport-1)*7:InfoWeekReport*7]))
        print("Average sales of this week is : ", round(sum(monthlyReport[(
            InfoWeekReport-1)*7:InfoWeekReport*7])/len(monthlyReport[(InfoWeekReport-1)*7:InfoWeekReport*7]), 2))
    else:
        print("Invalid number")
    print()
    InfoWeekReport = int(input("What week do you want to see (1-4) : "))
print("Exit")

print()
