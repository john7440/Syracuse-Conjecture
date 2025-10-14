#!/usr/bin/env python
# -*- coding: utf-8 -*-


def validated_input():
    """
    This function take a user input,
    test if it's a valid input (positive number which is not 0 or 1),
    then it call conjecture function, otherwise
    it print an error message and ask user again.

    :return: call the conjecture function or print an error message.
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



def conjecture(number):
    """We calculate the syracuse's conjecture which is:
        case 1 : n is even , then we divide by 2
        case 2 : n is odd, then we multiply by 3 and add 1

    :param number: initial value validate
    :return: a formated string with the list, number of steps needed
     Optional: maximal altitude and flying time
    """
    # We create a copy of the initial number to calculate 'flying time' later
    initial_number = number

    # We initialize a new variable 'flying_time' and set it to 0
    flying_time = 0

    # We initialize a new list that will contain each steps
    new_list = []

    # A while loop that stop when the actual number is 1
    while number != 1:
        new_list.append(number)

        if number % 2 == 0:
            number //= 2
        else:
            number = number * 3 + 1


    # OPTIONAL part
    # A for loop to determinate the flying time which is the first time
    # a value is lower than the initial value
    for actual_value in new_list:
        if actual_value < initial_number:
            flying_time = actual_value
            break

    formated_list = ' -> '.join([str(value) for value in new_list])
    return f'{formated_list}\nNumber of steps: {len(new_list)}\nMax Altitude: {max(new_list)}\nFlying Time: {flying_time}'


def main():
    """
    This is the main function.
    We call the input_validation function to valid the user input.
    :return: call the conjecture function with the valid input and print it
    """
    valid_input = validated_input()
    print(conjecture(valid_input))

if __name__ == '__main__':
   main()

