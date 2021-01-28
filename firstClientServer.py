from Menu import Menu
from TimeClass import Time

menu = Menu()
menu.add("Get Time", Time().GetTime)
menu.add("Get Time Without date", Time().GetTimeWithoutDate)
menu.add("Get Time Without date Or Seconds", Time().GetTimeWithoutDateOrSeconds)
menu.add("Get Year", Time().GetYear)
menu.add("Get Month And Day", Time().GetMonthAndDay)
menu.print()

try:
    userInput = int(input("What date and time would you like to get ?"))
    print(menu.select(userInput))

except ValueError:
    print("No.. input is not a number. Type 1 - 5")

