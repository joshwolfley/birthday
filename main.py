from Main_Functions import *
import datetime

current_date_and_time = datetime.datetime.now()
current_date = current_date_and_time.date()
current_time = current_date_and_time.time()
print(current_date)
print(current_time)

print("Welcome to the Age Generator!")
print("How old are you really...?")
print("")

first_menu()
user_input = get_user_input()


while True:

    if user_input == "0":
        break
    elif user_input == "1":

        first_name = input("What is your first name?") # How to repeat until they put in the right number.
        last_name = input("What is your last name")
        user_birth_year = 0

        try:
            user_birth_year = int(input("What year were you born?"))
            user_birth_month = int(input("What month were you born?"))
            user_birth_day = int(input("What day were you born?"))
        except ValueError:
            print("Enter 4 digit number for the year")

        user_birthday = current_date
        user_birthday = user_birthday.replace(year=user_birth_year, month=user_birth_month, day=user_birth_day)
        diff = current_date - user_birthday
        age_years = current_date.year - user_birthday.year
        age_months = current_date.month - user_birthday.month
        age_days = user_birthday.day - current_date.day

        print("----------------------------------")
        print("Well {} {}, here are your results!".format(first_name, last_name))
        print("Birthday: {}-{}-{}".format(user_birthday.month, user_birthday.day, user_birthday.year))
        print("You are {} years and {} month(s)".format(age_years, age_months, age_days))
        print("---------------------------------")

        main_menu()
    user_input = get_user_input()

print("Goodbye!")
