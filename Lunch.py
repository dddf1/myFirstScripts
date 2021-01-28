import sys
import random
import datetime

date = datetime.datetime.today().weekday()
#print(date)
resturants = ["Shuk", "Hmim Taim Naki", "BBB", "DotLiv", "Garrage", "Shuk - Indian", "Miznon", "Avangard", "Tiger Lily", "Butke"]
tuesday = "Zchuchiyot"
ranDay =random.choice(resturants)
weekend = "If you here on Friday get yourself something good..."

try:
    if date == 1:
        print(tuesday)
    elif date == 0 or date == 2 or date == 3:
        print(ranDay)
    elif date == 4 or date == 5:
        print(weekend)
    else:
        print("There are 7 days in a week. Please type 1 for Sunday, 2 for Monday, etc.")


except ValueError:
    print("No.. input is not a number. Type 1 for Sunday, 2 for Monday, etc.")