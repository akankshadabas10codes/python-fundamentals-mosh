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

## Ternary operators
age = 22
if age >= 18:
    message = "eligible"
else:
    message = "not eligible"
print(message)

# we can write the above code in a more concise way using ternary operators.
message = "eligible" if age >= 18 else "not eligible"
print(message)


## Logical Operators
# in python we have 3 different logical operators: and, or, not.

# imagine we are building an application for processing loans
high_income = False
good_credit = True
student = False

if high_income and good_credit:
    print("eligible")
else:
    print("not eligible")

# in the and operator, if both conditions are true, then the result is true.
# in contrast for the or operator, if at least one of the conditions is true, the
# result will return true.
if high_income or good_credit:
    print("eligible")
else:
    print("not eligible")

# now we will look at the not operator
# the not operator negates / inverses the result of a boolean expression.
if not student:
    print("eligible")
else:
    print("not eligible")

if (high_income or good_credit) and not student:
    print("eligible")
else:
    print("not eligible")


## Short circuit evaluation
high_income_one = True
good_credit_one = True
student_one = True

# one thing to note about the boolean operators is that they are short circuit.
# the python interpreter goes through all these arguments to see that they are true,
# however if one of the arguments are false, the evaluation stops.
# for instance if we change high_income_one to false, when the interpreter evaluates
# the args and the first one is false,the result of the entire expression is false.
if high_income_one and good_credit_one and not student_one:
    print("eligible")

# similarly for the or operator, the evalution of thes arguments stop when
# one of the arguments is true.


## chaining comparison operators
# lets say we want to implement a rule that saya age should be between 18 and 65.
age = 22
# if age >= 18 and age < 65:
if 18 <= age < 65:
    print("Eligible")

# usually in math we cna write 18 <= age < 65


# Quiz questions
if 10 == "10":
    print("a")
elif "bag" > "apple" and "bag" > "cat":
    print("b")
else:
    print("c")

# we would see c printed when we run this program.
# the first statement is false because 10 != "10" because they are both of different types.
# "bag" > "apple" is true because when we sort these words, bag comes after apple.
# "bag" > "cat" is false because bag comes before cat. Therefore since one of the statements
# is false, then the whole statement becomes false.


## For Loops
print("Sending a message")
# we use loops to create repetition
# lets say we want to call this statement 3 times
# we call the built in functions range and pass the argument as 3.
for number in range(3):
    print("Attempt")
# number is a variable of type integer.
# now if we add number in the print statement, we get a for loop where each iteration shows the message
# and the number of iteration it is at.
for number in range(3):
    print("Attempt", number)
# we can make this more meaningful / userfriendsly by adding number + 1
for number in range(3):
    print("Attempt", number + 1)

# we can make this cool effect as well
for number in range(3):
    print("Attempt", number + 1, (number + 1) * ".")
# we can also change the range to be from 1, 4 so we dont have to add number + 1,
# because now number willstart with 1.
for number in range(1, 4):
    print("Attempt", number, number * ".")

# we can add a third argument as a step
for number in range(1, 10, 2):
    print("Attempt", number, number * ".")

## For else

# consider that we were succesfully able to print the message.
# now we want to jump out of this loop.

# successful starts as False, so the task has not succeeded yet.
# The loop runs 3 times because range(3) gives 0, 1, and 2.
# Each time, it prints "attempt".
# Since successful is False, the if statement never runs and break never happens.
# Because the loop finishes without break, the else block runs at the end.
successful = False
for number in range(3):
    print("attempt")
    if successful:
        print("Sucessful")
        break
else:
    print("attempted 3 times and failed.")


## Nested Loops
# outer loop
for x in range(5):
    # inner loop
    for y in range(3):
        print(f"({x}, {y})")

## Iterables
print(type(5))
# range is an example of those complex types from python's primitive types.
print(type(range(5)))
# this range object is iterable which means we can iterate over it and use it in a for loop.
# strings and list are also iterable
for x in "Python":
    print(x)

for x in [1, 2, 3, 4]:
    print(x)


## While loops
# we use this loop to repeat somethign as a long as a condition is true.
# in this case we are evaluating a conditiona and then repeating a task
number = 100
while number > 0:
    print(number)
    number //= 2

command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)

## Infinite Loops
# a loop that runs forever
while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break
# this code above shows that this will run forever
# so to jump out of this we need a break statement

## Exercise
count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"We have {count} even numbers.")
