# Loopimg/Iterations:
# Occurs when a code block is executed a number of times(infinite) depending on a condition

# In python we have 2 types:
# 1. for loop
# 2. while loop

# 1. for loop:
# syntax: for variable in sequnce,string, range():
#                statements

# Worst Scenario
print("Welcome")
print("Welcome")
print("Welcome")
print("Welcome")
print("Welcome")

# Best Scenario
# 1.range(number)
# variable print_message is an index(starts from zero)
# range(50): Condition to check wether the index has exceeded 50
# range(start, limit, step)
# range(start, limit)
# range(limit)

# for print_message in range(100):
#     print(f"Welcome {print_message}")


# print numbers starting from 10 to 100 with interval 10

for numbers in range(10,100, 10 ):
    print(numbers)

