## Comparison Operators
# we use comparison operators to compare values.
# Such as shown below using the interactive shell:
# >>> 10 > 3
# True
# >>> 10 >= 3
# True
# >>> 10 < 20
# True
# >>> 10 <= 20
# True
# >>> 10 == 10
# True
# >>> 10 == "10"
# False

# for the last one, we get false because the values have different types and they
# are stored differently in computer memory.

# so when we do this now:
# >>> 10 != "10"
# True


# we can also use comparison operrators with strings.
# >>> "bag" > "apple"
# returns True. because when we sort these 2 words,
# "apple" comes before "bag", so "bag" is greater than "apple".
# but when we do "bag" == "BAG", we get false because every character
# has a numeric representation in computer memory,

# to find out the representation of a character, we can use the ord() function.
# >>> ord("b") is 98.
# >>> ord("B") is 66.
# so when we compare "bag" and "BAG", we are comparing the numeric representation
# of each character, and since "b" has a greater numeric representation than "B",
# we get true for "bag" > "BAG", but we get false for "bag" == "BAG" because they are not the same string.

## Conditional Statements
# after if we add a condition, which is bascially a boolean expression
temperature = 15
# if this boolean expression is true, the following block of code will
# be executed, otherwise it will be skipped.
if temperature > 30:
    print("it's wamrm.")
    print("drink some water.")
# if we want multiple conditions, we can use elif and else.
elif temperature > 20:
    print("it's nice.")
# if none of the previous statements are true, the else block will be executed.
else:
    print("it's cold.")
# this statement will be executed despite the fact that the condition
# is false, because it is not part of the if block.
print("done.")
# at first when we were writing the if statement the indentation was only 2 spaces
# but after we write our code and save it, the indentation increased to 4 spaces
# because that is what pep 8 reccomends. pep 8 is a style guide for python code.
