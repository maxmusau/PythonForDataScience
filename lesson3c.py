# Dictionaries: stored in key-value pair
# Syntax: curly braces -> {}
# Properties: unoredered, no duplicates, changaable/mutable

# {key(left) -> string : value(right) -> any data type}


student = {
    
            "first_name": "ERIC",
           "age": 37,
           "course": "Data Science",
           "GPA": 3.17,
           "subjects": ["Python", "Stats", "ML", "AI"]
           
           }

print(type(student))

# Operations
# 1. Accessing Items
# We use the key to Access the values
print(student["course"])

# access subjects
print(student["subjects"])

# Add a new subject: "DL"
student["subjects"].append("DL")

print(student["subjects"])

#1. Add a new items: the key should be unique, otherwise its a duplicate

student["has_completed"] = False
print(student)

# 2. Update(we use an existing key and assign it a new value)
student['age'] = 40
print(student)

# 3. Delete a pair
student.pop("first_name")
print(student)

# Clear all items in a dictionary
student.clear()
print(student)


# DataFrame and Series
# List and Dictionary