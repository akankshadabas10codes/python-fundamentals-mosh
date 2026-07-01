## square brackets define a list of a sequence of objects
# in betweeen these brackets we can have an object of any type like a list of strings, ints, bool, a list of lists
letters = ["a", "b", "c"]
matrix = [[0, 1], [2, 3]]
zeros = [0] * 5
print(zeros)
combined = zeros + letters
numbers = list(range(20))
chars = list("Hello World")
print(len(chars))
print(numbers)
print(combined)
letters[0] = "A"
## acessing items
print(letters)
print(letters[0])
print(letters[-1])
# this returns the first 3 elements of the list, the first index is inclusive and the second index is exclusive
print(letters[0:3])
print(letters[:3])
print(letters[1:])
print(letters[::2])

# fo instance we have
numbers = list(range(20))
print(numbers[::2])
# this will give a list of all the even numbers

## list unpacking
numbers = [1, 2, 3, 4, 5, 5, 6]
# first, second, third = numbers
# what we have above is the same thing as the code we have below
# whats important is that the number of items that we have on the left side of the operator,
# should be the same side as the number of items in the list.
# first = numbers[0]
# second = numbers[1]
# third = numbers[2]

# now lets say our list of numbers has multiple elements and we want to
# unpack the list we cna do so by ccreating a list called others. with this syntax
# we will get the first and second items and everything else will be stored in the others list.
first, second, *others = numbers
print(first)
print(others)

# okay now what if we only care about the first and the last items?
first, *other, last = numbers
print(first)
print(last)
print(other)

## looping over lists
letters = ["a", "b", "c"]
items = [0, "a"]
for letter in letters:
    print(letter)

# what if we want to get the index of each item in the list?
# we have a built in function called enumerate.
# this returns an enumerate object which is iterable. in each iteration,
# this object will return a tuple.
# a tuple is like a list but its read only, we cant change or add new items to it.
for letter in enumerate(letters):
    print(letter[0], letter[1])
