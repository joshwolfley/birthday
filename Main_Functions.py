def first_menu():
    print("Menu: ")
    print("0 - quit program")
    print("1 - try it out")


def main_menu():
    print("Menu: ")
    print("0 - quit program")
    print("1 - play again")


def get_user_input():
    try:
        user_input = input("What would you like to do?")
    except ValueError:
        print("Wrong")
    return user_input
