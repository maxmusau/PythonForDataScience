# RANGE
# ADD AN ITEM
# ADD ITEM AT POSITION
# REPLACE/UPDATE
# DELETE AN ITEM
# DELETE AN ITEM AT SPECIFIC POSITION

# Python For Data Science
# Lists
# Tuples
# Dictionary
# Decision Making


# RANGE -> :

locations = ["Westland", "Embakasi", "Karen", "Donholm", "Kitengela", "Kasarani"]

# Display all locations starting fro the second item [index:]
print(locations[1:])

# Display Data Upto a Certain Position(The last index is always excluded)

print(locations[:2])

# Range with start and end: Emba, Kite
print(locations[1:5])

# Return all the items: -> :
print(locations[:])


# Modifiable/Mutable -> Add, Update, Delete

languages = ["JavaScript", "Python", "Java", "Kotlin", "PHP"]

# Add: C++, C#
# append()
languages.append("C++")
languages.append("C#")

# extend()
# create a new list add 
more_languages = ["Ruby", "Go", "Pearl"]
languages.extend(more_languages)

print(languages)

# append(), extend() by default adds items to the end of the list
# To add item at a certain position -> insert()
# insert C at postion 3

languages.insert(2, "C")
print(languages)

# Update/Replace(Transformation)
languages[1] = "Python3"
print(languages)

# Delete:
# 1. pop() -> Delete the last item
languages.pop()
print(languages)

languages.pop()
print(languages)

# 2. Remove item with position
languages.pop(2)
print(languages)

# Delete all the items -> clear()
languages.clear()
print(languages)

# Remove by the name
languages.remove("Kotlin")
print(languages)

# CRUD: Create, Read, Update, Delete
