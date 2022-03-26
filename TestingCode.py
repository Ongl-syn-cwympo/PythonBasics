# Testing code
# Python code 
# Created by Ongl syn cwympo 
# https://github.com/Ongl-syn-cwympo

# How can we test this code? 

def add (number, another_number):
    return number + another_number

# Step 1
# Come up with some edge cases
# Invalid input -> enter a 'char' vs. an 'int' 

# Step 2
# Wrap in a try-catch block to handle any errors

try: 
    result = add('a', 9)
except Exception as error:
    print('input must be a number only')
    print(error)
else:
    print(result)
    
