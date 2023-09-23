print("Hello World")
print("Welcome to Python Programming")


# Comment:Igonored
# Variables: Store values
course = "Artificial Intelligence"
cost = 2000

print(course)
print(cost)

# Operators: Symbols or keyword used to perform operations
# 1. Arithmetic: +, -, /, *
# 2. Comparison Operators : (<, >, <=, >=, ==, !=)
# They are used to check relationship between variables/values(conditions), they return Two Instances(True or False)

variable1 = 100
variable2 = 200
print(variable1 > variable2)
print(variable1 < variable2)
print(variable1 <= variable2)
print(variable1 >= variable2)
print(variable1== variable2)
print(variable1 != variable2)

# Simple Login System
registred_password = "123456"
user_password = "12345"#

registered_username = "admin"
received_username = "admin"

print(registred_password == user_password)
print(registered_username == received_username)

# Logical Operators: and, or, not
# Used to check relationship bewtween condition
# and: Return True only when BOTH conditions return True, otherwise False
# or : Returns True, when ATLEAST one condition is True, but returns False when BOTH are False

print(registered_username == received_username   and   registred_password == user_password)