### Dictionaries -> key value pair (objects)

dict = { "a" : 1, "b" : 2, "c" : 3}

# accessing
print(dict["a"])
# changing
dict["b"] = 8

# storing dictionary values in a list
value_list = list(dict.values())
key_list = list(dict.keys())

# deleting a key
del dict["c"]

# iterating over dictionary
for key in dict:
    print(key, dict[key])


for key, value in dict.items() :
    print(key, value)