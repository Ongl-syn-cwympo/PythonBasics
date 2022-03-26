# If Statement ~ A programming conditional statement that, if proved true or false, will perform a function or displays information.
# Python code 
# Created by Ongl syn cwympo 
# https://github.com/Ongl-syn-cwympo

#programs make decisions based on control logic (control flow)

Class_Average_Grade = 90 # Change value here for different output

if Class_Average_Grade > 90 or Class_Average_Grade == 90:
    print("Class average grade is an A*")
elif Class_Average_Grade < 90 and Class_Average_Grade > 80:
    print ("Class average grade is an A")
elif Class_Average_Grade < 80 and Class_Average_Grade > 70:
    print("Class average grade is an B")
elif Class_Average_Grade < 70 and Class_Average_Grade > 50:
    print("Class average grade is an C")    
else: 
    print("Class average grade is a D, F or U")
    
