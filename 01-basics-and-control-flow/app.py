## Strings in Python
course = "Python Programming"
# finding the length of the string
print(len(course))
# next we want to find out a particular character in the string, we use
# square brackets and the index of the character we want to find
course[0]
# the index starts with 0, so the first character is at index 0,
# the second character is at index 1, and so on.
# So if we want to find the first character of the string, we use course[0].
# If we want to find the second character, we use course[1], and so on.
# In this case, course[0] will return 'P', which is the first
# character of the string "Python Programming".
print(course[0])
# we can also do an index of -1. if 0 represents the first character, -1 represents the last character.
# So if we want to find the last character of the string, we can use course[-1].
# In this case, course[-1] will return 'g', which is the
# last character of the string "Python Programming".
print(course[-1])
# next we will learn how to slice a string.
# slicing a string means to extract a part of the string.
# we can use the slice operator, which is a colon (:), to slice a string.
# the syntax for slicing a string is: string[start:end]
# where start is the index of the first character we want to include in the slice,
# and end is the index of the first character we want to exclude from the slice.
# For example, if we want to slice the string "Python Programming" to get the word
# "Python", we can use the slice operator like this: course[0:6]
# In this case, course[0:6] will return 'Python', which is the substring of the string "Python Programming" that
# starts at index 0 and ends at index 5.
print(course[0:6])
# now what if we do not include the end index in the slice? For example, if we do course[0:],
# what will it return?
# If we do not include the end index in the slice, it will return the substring from the start index to the end of the string.
# So in this case, course[0:] will return 'Python Programming', which is the entire string "Python Programming" because we did not specify an end index.
print(course[0:])
# now what if we do not include the start index in the slice? For example, if we do course[:6],
# what will it return?
# If we do not include the start index in the slice, it will return the substring from the beginning of the string to the end index.
# So in this case, course[:6] will return 'Python', which is the substring of the string "Python Programming" that starts at the beginning of the string and ends at index 5.
print(course[:6])
# we can also use negative indices in slicing. For example, if we do course[-11:-1],
# what will it return?
# If we use negative indices in slicing, it will return the substring from the end of the string to the beginning of the string.
# So in this case, course[-11:-1] will return 'Programming', which is the substring of the string "Python Programming" that starts at index -11 and ends at index -2.
print(course[-11:-1])

## Escape Sequences in Python
# an escape sequence is a sequence of characters that represents a special character.

course = 'Python "Programming"'
# in this case, we want to include double quotes in the string,
#  so we use the backslash (\) to escape the double quotes.
#  The backslash tells Python that the next character is a
# special character and should be treated differently.
print(course)
# backslash is an escape character and backslash followed by a quote is an escape sequence.
# here are a list of some common escape sequences in Python:
# \n - new line
# \t - tab
# \\ - backslash
# \' - single quote
# \" - double quote
# \r - carriage return
# \b - backspace
# \f - form feed
# \v - vertical tab
# \ooo - octal value
# \xhh - hexadecimal value

# Formatting Strings in Python
first = "akanksha"
last = "dabas"
full = first + " " + last
print(full)
# or we can use formatted strings like showns
full_name = f"{len(first)} {2+2}"
print(full_name)

# String Methods in Python
course = "Python Programming"
print(course.upper())
print(course.lower())
# the title() method converts the first character of each word
# to uppercase and the rest of the characters to lowercase.
print(course.title())
# this is used to remove any leading or trailing whitespace from the string.
print(course.strip())
print(course.find("Programming"))
print(course.replace("Python", "Java"))
print("pro" in course)
print("swift" not in course)

# Numbers in Python
# in python we have 2 types of numbers, integers and floats.
x = 1
x = 1.1
# we also have complex numbers. In math they are in the form a + bi,
# where a is the real part and b is the imaginary part. In python, instead
# of i, we use j to represent the imaginary part.
x = 1 + 2j

# standard arithmetic operators
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
# we actually have 2 types of division.
# with the division oeprator above, we get a float result.
# If we want to get an integer result, we can use the floor division operator (//).
print(10 // 3)
# the modulus operator (%) returns the remainder of the division.
print(10 % 3)
# the exponentiation operator (**)
# returns the result of raising the first operand to the power of the second operand.
# in other words, "left to the power of right".
print(10**3)


# augemented assignment operators
x = 10
# lets say we want to incremennt the value of 10 by 3. We can do it like this:
x = x + 3
print(x)
# or we can use the augmented assignment operator like this:
x += 3
print(x)

## Working with numbers in Python
print(round(2.9))
print(abs(-2.9))
# if we want to write a program that involves complex mathematical calculations,
# we need to use the math module. A module is like a separate file with some
# python code. It includes lots of mathematical functions for working with
# numbers. But we need to import this module, in order to use it. So
# at the top of the file, we can write "import math" to import the math module.
import math

# math in this program is an object, so we can a dot notation to see all the
# functions more accurately.
print(math.ceil(2.2))
# as we can see, the ceil() function rounds a number up to the nearest integer. Since it was
# 2.2, it rounds it up to 3. But Why? Because the ceil() function always rounds a number
# up to the nearest integer, regardless of whether the number is closer to the
# lower or higher integer. So in this case, even though 2.2 is closer to 2 than
# it is to 3, the ceil() function will still round it up to 3 because that is the nearest
# integer that is greater than or equal to 2.2.


## Type conversion in Python
# x = input("x: ")
# y = x + 1
# as we can see this is wrong because the input() function returns a string,
# and we cannot add an integer to a string.
# we can find the type of a variable using the type() function.
# x = input("x: ")
# print(type(x))
# wecna also convert / concatenate a variable of one type to another type.
# int(x) - converts a string to an integer
# float(x) - converts a string to a float
# str(x) - converts a number to a string
# bool(x) - converts a value to a boolean
# therefore to fix this we need to convert x into an interger.
x = input("x: ")
y = int(x) + 1
print(f"x : {x}, y : {y}")
# in this case we are using a formatted string because we want to include the values of x
# and y in the string. The f before the string indicates that it is a formatted string,
# and the curly braces {} are used to include the values of x and y in the string.
# So in this case, if we input 10 for x, the output will be "x : 10, y : 11".


# Falsy values in Python
# "" - empty strings are considered falsy, interpreted as a boolean false.
# 0 - the integer 0 is considered falsy, interpreted as a boolean false.
# None - the None value is considered falsy, interpreted as a boolean false.
# whenever we use these values in boolean context, we will get false.
# for instance in an interactive shell, if we have the value bool(0), it will
# return false, but if we do bool(1) / bool(-1), it will return true
# because any non-zero integer is considered truthy. Similarly if we do it for
# empty string, bool("") will return false, but bool(" ") will return true because it is not an empty string.

# Quiz
# Q: What are the built in primtive types in Python?
# A: We have strings, numbers (integers, floats, complex), and booleans (True and False).

# Q: We have this variable fruit set to "Apple". What will we see in the terminal, when we print
# fruit[1]?
fruit = "Apple"
print(fruit[1])
# A: We will see "p" in the terminal, because the index starts at 0, so the first
# character "A" is at index 0, and the second character "p" is at index 1.

# Q: What will we see in the terminal, when we print fruit[1:-1]?
print(fruit[1:-1])
# A: We will see "ppl" in the terminal, because the slice operator [1:-1] will
# return the substring from index 1 to index -2, which is "ppl". Rmb that the end
# index is exclusive, so it will not include the character at index -1, which is "e".

# Q: What is the result of this expression:
print(10 % 3)
# A: The result of this expression is 1, because the modulus operator (%)
# returns the remainder of the division of 10 by 3.

# Q: What will we see when we print:
print(bool("False"))
# A: We will see True in the terminal, because any non-empty string is considered truthy.
