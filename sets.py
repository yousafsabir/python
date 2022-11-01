### Sets -> unordered, unique element, unordered, unchangeable*, and unindexed.
# unchangeable: you can add to set and you can only remove it by value, no index

# if we want to initialize an empty set
set = set()
# A set with value
set2 = {1, 2, 3}

# Add/ remove from sets
set2.add(5)
set2.remove(2) # removes 2 if present

# Check existance of a value
print(2 in set2) # happens much faster than a list
