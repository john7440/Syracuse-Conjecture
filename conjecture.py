#!/usr/bin/env python
# -*- coding: utf-8 -*-


def ask_for_number():
    """
    This function asks the user to enter a number and verify it.
    :return: the validated number.
    """
    # User input which must be a positive int (which is not 0 or 1)
    # else it returns an error and ask the user again
    while True:
        user_input = input("Please enter a positive integer: ")
        if user_input.isdigit() and int(user_input) != 0 and int(user_input) != 1:
            user_input = int(user_input)
            break
        else:
            print('Sorry invalid input')
    return user_input


def syracuse_sequence(number):
    """This function calculate the syracuse's conjecture which is:
        case 1 : n is even , then we divide by 2.
        case 2 : n is odd, then we multiply by 3 and add 1.
    :param number: initial value validate.
    :return: values and the flying time.
    """
    # We create a copy of the initial number to calculate 'flying time' later
    initial_number = number
    values = []

    while number != 1:
        values.append(number)

        if number % 2 == 0:
            number //= 2
        else:
            number = number * 3 + 1

    # OPTIONAL part:
    flying_time = sum(1 for value in values if value > initial_number)

    return values, flying_time


def display_syracuse_sequence(values, flying_time):
    """
    This function display the results of the syracuse's conjecture.
    :param values: the values at each step.
    :param flying_time:the flying time.
    :return: a formatted string.
    """
    formated_list = ' -> '.join([str(value) for value in values])
    print(f'{formated_list}\nNumber of steps: {len(values)}\nMax Altitude: {max(values)}\nFlying Time: {flying_time} steps')


def main():
    """
    This is the main function.
    """
    number = ask_for_number()
    values, flying_time = syracuse_sequence(number)
    display_syracuse_sequence(values, flying_time)


if __name__ == '__main__':
   main()

