### Operators
# == equality checker
# != enequality checker
# >=
# <=
# >
# <
### Chaining Conditionals
# and
# or
# not

### order of chaining
# not proceeds first
# and proceeds secondly
# or proceeds last

print("a" > "Z") # prints true. Python compares ascii code
print(ord("a")) # prints ascii code of a

### if else
# if condition:
#     indented Block
# elif condition:
#     indented Block
# else:
#     indented Block

name = 'yousaf'
if name == "yousaf":
    print("you are great")
elif name == "ismail":
    print("you are great too")
else:
    print("helloworld")
