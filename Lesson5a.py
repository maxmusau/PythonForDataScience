# Nested Condition: When another condition is checked after checking the top-most condition

# Algorithm: Banking System
# The PIN is checked first(top most)
# Then for withdrwals, you need to have a balance in your account

database = {
    "pin": 5413,
    "balance": 10000,
    "status": True
}

requested_pin = int(input("Enter Your PIN?: "))

if requested_pin == database["pin"]:
    print("SUCCESS!")
    print("You Can Now Withdraw....")
    amount = int(input("Enter the Amount?: "))
    
    if amount <= database["balance"]:
        print(f"Confirmed You have withdrawn {amount}")
        acc_balance = database["balance"] - amount
        print(f"Your ACC Balance is {acc_balance}")
    else:
        print("Insuffient Balance...")
else:
    print("WRONG PIN!!!")