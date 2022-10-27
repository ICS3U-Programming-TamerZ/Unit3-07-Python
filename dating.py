#!/usr/bin/env python3

# Created By: Tamer Zreg
# Date: Oct. 18, 2022
# This program decides if you can date someone's grandchild using
# a compound boolean expression


def main():

    # Setting age range variables
    min_age = 25
    max_age = 40

    # Gets the user's age
    user_age = input("Enter your age: ")

    # Tries to cast user_age to type float
    try:
        user_age_int = int(user_age)
        if user_age_int > min_age and max_age > user_age_int:
            print("Please date my grandchild!")
        else:
            print("Get lost!")

    # Exception thrown if user_age is not a number
    except ValueError:
        print("You must enter your age as a number.")
        main()


if __name__ == "__main__":
    main()
