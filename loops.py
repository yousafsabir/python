# for loop
for i in range(10):
    print(i)

# range() :-
#   it actually creates a list which for loop iterates over
#   3 parametes, start, stop, step

list = [1, 2, 3, 4, 5]

for elem in list: 
    print(elem)

for i in range(len(list)):
    print(i)

for i, elem in enumerate(list):
    print(i, elem)



### While Loop

i = 0
while i < 10:
    print(i)
    i += 1