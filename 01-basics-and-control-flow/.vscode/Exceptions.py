## Exceptions
# define a list of numbers with 2 elements
# numbers = [1, 2]
# print(numbers[3])
# this line above thhrows and error for "list index out of range"

# input() returns the user's answer as a string.
# int() converts that string into an integer.
# This allows us to use age in calculations and number comparisons.
# age = int(input("age: "))
# if we type in "a" we get a type value error

## Handling exceptions
# when python sees a try block, it will execute every statement in the block,
# if any of these statements throws an exception the code in the except caluse will
# be executed. if you do not have any code exceptions then the except line will not be printed.
try:
    age = int(input("Age: "))
except ValueError as ex:
    print("You didn't enter a valid age")
    print(ex)
    print(type(ex))
else:
    # optional esle block: if no exceptions is thrown in the try block
    print("No exceptions were thrown.")
print("Execution continues")


## Handling different exceptions
# ZeroDivisionError: becasue in progrramming we cannot divide a number by 0
try:
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
# except ZeroDivisionError:
#     # print("Age can't be 0.")
#     print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown")

# one thing to note:
# when python executes the code that we have in the try block,
# if any of the statements throws an exception that matches one of
# the except clauses, that except caluse is executed and the other
# except clauses are ignored.


## Cleaning up and the with statment
try:
    # with statement also releases external sources
    # if an ibject has the exit and enter statment we can use the with statement
    with open("trial.py") as file:
        print("File opened.")
        file.__enter__
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid range.")
else:
    print("No exceptions were thrown")
