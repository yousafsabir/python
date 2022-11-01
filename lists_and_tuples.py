### Collections
# two tyes of collections, 1: lists (arrays) -> ordered , 2: tuples -> unordered

list_array = ["abc", 2, "hello", 4]

# List/Array Length
print("Length of the array" ,len(list_array))

# List methods
print(list_array[4]) # to access element at certain index
list_array[4] = "hello" # similarly, we can change value at index too
list_array.append("5") # adds/pushes "5" at the end
list_array.insert(0, "5") # adds/pushes "5" at the start
list_array.insert(3, "5") # will insert "5" at index 3
list_array.pop() # first removes then returns the last value
list_array.pop(0) # to remove first element
list_array.pop(3) # removes and returns element on 3rd index
list_array.extend([6, 7, 8]) # extends list with given array

# Check existance of a value
print("hello" in list_array) #prints boolean

# ! Important Note:
# lists in python are not passed by value, rather by reference, even if we assign them to other variable
arr = [1, 2, 3]
y = arr
arr.append(4)
print(y, arr) # it will print [1, 2, 3, 4] [1, 2, 3, 4]
# even though we've assigned it earlier,
# to actually make a copy
# we do this
x = arr[:]


### Tuples:- Just like lists, but immutable, we can only access data but not write

a_tuple = ("a", "b", "c")
print(a_tuple[2])