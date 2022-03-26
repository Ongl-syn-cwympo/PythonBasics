# Mathematical operations ~ Addition, Subtraction, Multiplication & Division
# Program can only handle 2 inputs
# Python code 
# Created by Ongl syn cwympo 
# https://github.com/iTsHackYouSate

print("Which mathamatical operation would you like to test?")
print("1. Adding")
print("2. Subtracting")
print("3. Multiplication")
print("4. Division")
print("4. Division with remainder")

Num = input()

if Num == "1":
  print("+ Addition +")
  x = input("Type a number: ") # Asks user for the input
  y = input("Type another number: ") # Asks user for the second input
  
  answer = int(x) + int(y) # This function adds both numbers inputed together
  
  print("The solution is: ", + answer) # This outputs the combined numbers

if Num == "2":
  print("- SUbtraction -")
  x = input("Type a number: ") # Asks user for the input
  y = input("Type another number: ") # Asks user for the second input
  
  answer = int(x) - int(y) # This function subs both numbers inputed together
  
  print("The solution is: ", + answer) # This outputs the subtracted numbers

if Num == "3":
  print("* Multiplication *")
  x = input("Type a number: ") # Asks user for the input
  y = input("Type another number: ") # Asks user for the second input
  
  answer = int(x) * int(y) # This function multiplies both numbers inputed together
  
  print("The solution is: ", + answer) # This outputs the multiplied numbers

if Num == "4":
  print("/ Division /")
  x = input("Type a number: ") # Asks user for the input
  y = input("Type another number: ") # Asks user for the second input
  
  answer = int(x) / int(y) # This function divides both numbers inputed together
  
  print("The solution is: ", + answer) # This outputs the divided numbers

#modulus operator - gives you the remainder left over after a division

if Num == "5":
  print("/ Division with remainder /")
  x = input("Type a number: ") # Asks user for the input
  y = input("Type another number: ") # Asks user for the second input
  
  remainder_after_division = x % y 
  print("Remainder after the division = ", remainder_after_division)
