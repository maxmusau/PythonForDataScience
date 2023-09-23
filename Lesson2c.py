# Numbers : Arithmetics -> Integers, Floats, Complex
# Integers: Values without decimal places

age = 36
print( type(age) )

# Floats:
distance = 20.6
print( type(distance) )


# Inputting values to the System:
# We use input("Instructions")
# String -> input() or str(input("Instructions") )
# Integer -> int( input("Instructions") )
# Floats -> float( input("Instructions") )

# Simple Interest
# principal -> int
# rate -> float
# time -> int

try:
    name = str(input("Please Enter Your Name "))
    principal = int( input("Please Enter Your Principal ") )
    rate = float( input("Please Enter the rate ") )
    time = int( input("Please Enter the Time ") )

    interest = principal * rate * time
    print(f"{name} Your interest is {interest}")
except:
    print("Something went wrong....")

# Exception Handling try--catch block