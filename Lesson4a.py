# Control Stuctures
# Conditional Control Structures
# Iterative 

# Control Stuctures: It determines the order in which programs are executed
# a) Skip some programs while executing other -> condition
# b) Repeat the execution of some codes -> Looping

# By default: Python performs a sequential control structure, codes dont have indentations

# print("Python")
# print("Python")
# print("Python")
# print("Python")

# b) Control Stuctures: Codes are executed based on conditions -> if, if..else, if..elseif..else

#1. if : 
# syntax:
# if condition:
#     statemnt/body

# 2. if..else
# syntax:
# if condition:
#    statements(if)
# else:
#   statement(else)


number = -1
if number < 0:
    print("Number is Negative")
else:
    print("Number is Positive")
    
username = input("Enter Username: ")
password = input("Enter Password: ")

if username == "admin" and password == "admin123":
    print("=====ACCESS GRANTED======")
else:
    print("=====ACCESS DENIED======")
    

    
    
    