# LIST DATA TYPES: Used to store collection of values on the same variable

# Bad Sceneraio
county1 = "Nairobi"
county2 = "Bomet"
county3 = "Samburu"

# Best Scenario
counties = ["Nairobi","Bomet", "Samburu"]
years = [2015, 2019, 2021, 2023]
student = ["Jane", 21, False, 150000.0, ["0791123456", "0786123456"] ]
print(type(counties))
# Properties: Uses sq brackets [], items comma separated
# Other Properties: Ordered(indexing), Modifiable/Changeable, Allows Duplicates

# 1. Ordering: Each item is given an index value starting from zero []
print(counties[2])
# accessing a nested list
print(student[4][1])

# Task:
customer = ["Derrick", ["Nairobi", "Kisumu", "Kilifi"], ["derrick@gmail.com", ["0712345678", "0723567891"]]]
# Using Indexing:
# a) Access the email
# b) All the contacts
# c) Access Kisumu
print(customer[2][0])
print(customer[2][1])
print(customer[1][1])

tensors = [  [1,2]  ,    3   ,     [   4,   [5, 6, [7,8]]  ]    ]
# access 6, 8, 3
print(tensors[2][1][1])
print(tensors[2][1][2][1])
print(tensors[1])


# RANGE
# ADD AN ITEM
# ADD ITEM AT POSITION
# REPLACE/UPDATE
# DELETE AN ITEM
# DELETE AN ITEM AT SPECIFIC POSITION

