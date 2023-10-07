#Program to Determine NHIF Contributions that Someone will Pay

salary = int(input("Enter the amount of salary you get:"))

if salary < 6000:
    print ("You are required to contribute: KES 150.00")
elif salary >= 6000 and salary < 8000:
    print("You are required to contribute: KES 300.00")
elif salary >= 8000 and salary < 12000:
    print("You are required to contribute: KES 400.00")
elif salary >= 12000 and salary < 15000:
    print("You are required to contribute: KES 500.00")
elif salary >= 15000 and salary < 20000:
    print("You are required to contribute: KES 600.00")
elif salary >= 20000 and salary < 25000:
    print("You are required to contribute: KES 750.00")
elif salary >= 25000 and salary < 30000:
    print("You are required to contribute: KES 850.00")
elif salary >= 30000 and salary < 50000:
    print("You are required to contribute: KES 1000.00")
elif salary >= 50000 and salary < 100000:
    print("KES 1500.00")
else : salary >= 100000
print("You are required to contribute: KES 2000.00")
