#!/usr/bin/env python3
# Created By: Maeva Tchuenga
# Date: 11, 02 2026
# Create a program that allows the user to enter a positive number.


def main():
    loop_counter = 0
    total = 0

    try:
        user_number = int(input("Enter a positive number: "))
        while loop_counter <= user_number:
            if user_number > 0:
                print(f"The sum of user inputs from 0 to {user_number} is: {total}")
                print("the user_input is a positive number.")
            total += user_number
            loop_counter += 1
        if user_number < 0:
            print(" user_input is a Negative number .")

        else:
            user_number == 0
            print("Zero is a positive integer.")

    except Exception:
        print("Sorry! user_input is not an integer.")


if __name__ == "__main__":
    main()
