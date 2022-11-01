### Slice operator 
# takes slice of a collection
arr = [1, 2, 3, 4, 5, 6, 7, 8]
y = ["how", "are", "you", "mate"]
str = "abcdef"


# syntax
# slice = [start: stop: step]

print(arr[4:]) # starts at 4 and ends at length
print(arr[0:4]) # start at 0 and end at 4 but not index 4
print(arr[::2]) # start at 0, end at length, step by 2
print(arr[::-1]) # start at 0, end at length, step -1 (reverse it in simple words)

# all this works in strings and tuples too

