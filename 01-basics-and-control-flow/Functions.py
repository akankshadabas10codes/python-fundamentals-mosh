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


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))


# ** args
# we are going to use this function to save information about the user
def save_user(**user):
    print(user["name"])


# with this we get key value pairs
# the object that we get once this is printed out is known as a dictionary.
save_user(id=1, name="John", age=22)


# Debugging
# *numbers means that the function cna accept any number of arguments
# python collects those arguemnts into a tuple called numbers.
# total = 1, we start at 1 becasue multiplying by 1 does not chnage a number
# total = 1
# total = 1 * 2 = 2
# total = 2 * 3 = 6
# and so on.. and then we return total whcih is the final result
def multiple(*numbers):
    total = 1
    for number in numbers:
        total *= number
        return total


print("Start")
print(multiple(1, 2, 3))

## shortcuts using mac
# to go to the extreme right or left we press fn and the right or left arrows
# similarly we can press fn and arrow up or down to either go to the extreme top or extreme bottom
## if we want to select a text and move it up or down we cna press down the option key and then up / down arrows
# we can comment and uncomment lines using command + /


### Exercise
# common interview question
# if the input we enter is divisible by 3 then it returns fizz
# if the input is divisible by 5 then it returns buzz
# if the input is divsible by both 3 and 5 then it will return fizz buzz
def fizz_buzz(input):
    if input % 3 == 0:
        result = "Fizz"
        # return "Fizz"
    else:
        result = "Buzz"
        # return "Buzz"
    return result
    # no return statement here for the return ones


print(fizz_buzz(3))


# another way to do this
# if the input is divsible by both 3 and 5 then it will return fizz buzz
def fizz_buzz(input):
    if input % 3 == 0:
        result = "Fizz"
    return "Buzz"
    # no return statement here for the return ones


def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input
    # no return statement here for the return ones


print(fizz_buzz(15))
