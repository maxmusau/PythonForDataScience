# Grading Systems
# if..elif..else

# 0 - 40 -> E
# 41 - 50 -> D
# 51 - 60 -> C
# 61 -70 -> B
# 71 - 100 -> A

# else -> Invalid!!! -> less than 0 and more 100

marks = int(input("Enter Score? "))
if marks >= 0 and marks <=40:
    print("E")
elif marks >= 41 and marks <= 50:
    print("D")
elif marks >=51 and marks <=60:
    print("C")
elif marks >=61 and marks <=70:
    print("B")
elif marks >=71 and marks <=100:
    print("A")
else:
    print("Invalid Marks!!!")
    
    
# Nested Conditions:
# Looping
    