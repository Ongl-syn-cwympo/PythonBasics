# Exceptions ~ An exception is an event, which occurs during the execution of a program, that disrupts the normal flow of the program's instructions.
# Python code 
# Created by Ongl syn cwympo 
# https://github.com/Ongl-syn-cwympo

# User input error - this throws an exception if a string is given by user
# Age = int(input("Enter your age:"))

# try-catch block 
try: 
    age = int(input("Enter your age:"))
except ValueError as error:
    print("please enter a number only")
    print(error)
else:
    print("no exceptions were thrown, excute this")
