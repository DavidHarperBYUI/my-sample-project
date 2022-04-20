
import math
from datetime import datetime
from datetime import date

current_date_and_time = datetime.now()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print(f"The current date and time is: {current_date_and_time:%Y-%m-%d}")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

w = float(input("Enther the width of the tire in mm (ex. 205): "))
a = float(input("Enter the aspect raio of the tire (ex. 60): "))
d = float(input("Enther the diameter fo the wheel in inches (ex. 14): "))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

v_1 = (w * a + 2540 * d)
v_2 = math.pi * w**2 * a * (v_1)
v_3 = v_2 / 10000000000

print(f"The volume of the tire is: {v_3 :.2f}")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

purchase = str(input("Would you like to purchase tires with these dimetions? (y/n): "))

if purchase == "y":
    phone = int(input("Please enter your phone number (no spaces, dashes, or slashes, ex. 505XXXXXXX: "))
    with open("Tires.txt", "at") as tire_volume:
        print(f"{current_date_and_time}, {w}, {a}, {d}, {phone}", file=tire_volume)
elif purchase == "n":
    with open("Tires.txt", "at") as tire_volume:
        print(f"{current_date_and_time}, {w}, {a}, {d}", file=tire_volume)
else:
    print("an error has occured.")