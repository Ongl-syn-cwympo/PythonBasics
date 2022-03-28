# Operators ~ not, and, or
# Python code 
# Created by Ongl syn cwympo 
# https://github.com/Ongl-syn-cwympo

# not operator
# Falsy values - empty string '' empty list [] 0 None - apply not to a false, get true
name = ''
if not name:
    print("Name is empty")
    
# and operator 
age = 18
if age >= 18 and age < 65: 
    print("You're eligable")
else:
  print("Not eligable")
    
# or operator 
age = 100
if age == 18 or age == 65: 
    print("You're eligable")
else:
  print("Not eligable")
  
