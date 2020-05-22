# Created by Will Osteen
# Student ID 001099825

from menu import print_menu
from delivery import delivery
# Package loading manually
# Load lists will be used to manually load trucks with packages
load_list1 = [1, 7, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 39, 40]
load_list2 = [3, 4, 6, 18, 22, 25, 26, 28, 32, 36, 38]
load_list3 = [2, 5, 8, 9, 10, 11, 12, 17, 21, 23, 24, 27, 33, 35]



# Runtime is O(n)
# Main interface for seeing package delivery
menu = True
while menu is True:
    print_menu()

    choice = None
    try:
        choice = int(input("Enter your choice [0-2]: "))
    except:
        print("\nInvalid input. Please enter a number between 0 and 2")
        continue

    if choice == 1:
        delivery(load_list1, load_list2, load_list3, 17, 0)
    elif choice == 2:
        try:
            print("\nYou will be asked to enter the time by hours, then minutes. Time is in military time.")
            hour = int(input("Please enter an hour [0-23]: "))
            min = int(input("Please enter the minutes [0-59]: "))
        except:
            print("\nInvalid input.")
            continue

        if hour > 23 or hour < 0:
            print("\nInvalid hour input. Hours will be set to 0")
            hour = 0
            continue
        if min > 59 or min < 0:
            print("\nInvalid minute input. Minutes will be set to 0")
            min = 0
            continue

        delivery(load_list1, load_list2, load_list3, hour, min)
    elif choice == 0:
        menu = False
    else:
        print("\nInvalid input. Please enter a number between 0 and 2")
