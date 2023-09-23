# Tuples: Syntax uses paranthesis -> ()
# Properties: immutable/unchangeable, ordered(indexing), allow duplicates

privileges = ("view_users", "generate_reciets", "delete_records")
print(type(privileges))

# create a tuple of single data
names = (1,)
print(type(names))

# ordered
print(privileges[1])

names.append("ajne")

