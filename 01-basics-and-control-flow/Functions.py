## Functions
def greet():
    print("Hi there")
    print("Welcome aboard")


greet()


## Arguments
# the difference between print and greet is that print takes in input
# while greet does not. In order to pass inputs lke first name and last name
# for this function. When defining a function, in between the parenthesis we
# define our parameters.
def greet(first_name, last_name):
    print("Hi there")
    print("Welcome aboard")


# when calling this function, we need to supply 2 values for those parameters
# we refer to them as arguments.
greet("josh", "luca")

# a parameter is the input that you define for your function
# where as an argument is the actual value for a given parameter.


def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")


# when calling this function, we need to supply 2 values for those parameters
# we refer to them as arguments.
greet("josh", "luca")

# note that by default, all the parameters you define for a function
# are required


def greet(name):
    print(f"Hi {name}")


# 1- Perform a task - print
# 2 - return a value - round


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Mosh")
print(message)
# witht this message variable we can print it on th terminal, write it to a file,
# send it in an email..
file = open("context.tzt", "w")
file.write(message)

# in python all functions by default return a None value unless we specifcially return a value
#  in the case that we do
print(greet("Mosh"))
# none is an object that represents the absence of a value
#


# for instance the exception is unless we return a value like
def greet(name):
    # print(f"Hi {name}")
    return "..."


## Keyword arguments
def increment(number, by):
    return number + by


# since increment returns a value we can store it in a variable like result and then print it on the terminal
result = increment(2, 1)
print(result)

# we can simplify this code, since we used the result variable only
# once, we cna try to remove it


def increment(number, by):
    return number + by


# since increment returns a value we can store it in a variable like result and then print it on the terminal
# the way this works is that when we run this code, the first it will call the increment function
# and then it will get th ereuslt and store it in avaraible for us that we won't see
# and then it will pass thta variable as an argument to the print function
print(increment(2, 1))


# we can also make this code more readable
# in the sence if someone were to look at the print statement they
# might not understand what it means with the 2 and 1, we cna do
# so if we are calling our code with multiple arguemnts, we cna
# make it more readable by doing so using keyword arguments like by = 1
print(increment(2, by=1))


## Default arguments
# lets say we do not always want to define the by argument in the increment function
# and we want to default it to a value
# we would change the function by this:
def increment(number, by=1):
    return number + by


print(increment(2))
