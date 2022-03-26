# Adding two random numbers together.
# Python code 
# Created by Ongl syn cwympo 
# https://github.com/Ongl-syn-cwympo

import random

# Main function 
def main_function():
    first_number = get_random(1, 50)
    second_number = get_random(51, 100)
    result = add(first_number, second_number)
    print(result)

# Helper function (subroutine)
def get_random(start, end):
    random_number = random.randint(start, end)
    return random_number

# Helper function #2 (subroutine)
def add(number, another_number):
    return number + another_number

# Call our main function to start the program
main_function()
