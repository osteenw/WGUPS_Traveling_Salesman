# Created by Will Osteen
# Student ID 001099825

def print_menu():
    print("\n==========================================================")
    print(f"=                   MAIN MENU                           =")
    print("==========================================================")
    print("Enter 1 to see packages at end of the day")
    print("Enter 2 to see packages at specific time")
    print("Enter 0 to exit")

# Prints status of every package
def print_status(package_list, time):
    print("========================================================================================================")
    print(f"=                                      ALL PACKAGES AS OF {time}                                        =")
    print("========================================================================================================")
    for package in package_list:
        print(package.package_string())