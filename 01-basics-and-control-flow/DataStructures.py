## square brackets define a list of a sequence of objects
# in betweeen these brackets we can have an object of any type like a list of strings, ints, bool, a list of lists
from itertools import count

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

# we can also do this
items = (0, "a")
index, letter = items
for index, letter in enumerate(letters):
    print(index, letter)


## Adding or removing items
letters = ["a", "b", "c"]
# add
# if we wnat to add an item to the end of the list, we should use the append method
# rmb earlier we learnt that everything in python is an object and therefore we can make use of
# the dot notation to access the individual functions / methods in that object
letters.append("d")
print(letters)
# if we want to add an item at a specific index, we should use the insert method
letters.insert(0, "-")
print(letters)


# Removie
# if we want to remove an item at the end of the list, we should use the pop method
letters.pop(0)
print(letters)

# when we want to remove an item but we do not know the index, we can use
# this removes the first occurence of that item in the list.
# if we want to remove all the occurences, we need to loop over this list
# and remove each item individually
letters.remove("b")
print(letters)

# another way to remove an item is using the word del
# we can delete just one item or a range of items
# this is the diff between the pop and the delete statement.
# the pop method will only delete the one item, but the del can delete a range of items
# del letters[0]
# del letters[0:2]
# finally if we wwnt to remove all the items in the list we should use the clear method
letters.clear()
print(letters)

# finding items
# we want to find the index of an item in the list
letters = ["a", "b", "c"]
# print(letters.index("a"))

# what if we want to find the index of an element that does not exist in the list?
# we get a value error, c based returns -1.
if "d" in letters:
    print(letters.index("d"))
print(letters.count("a"))

## Sorting lists
numbers = [3, 51, 2, 8, 6]
numbers.sort()
print(numbers)
# sorting in descending order
# numbers.sort(reverse=True)
# print(numbers)
# the sorted function returns a new list and does not modify the original list.
sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers)


# lets say we are building an application for processing orders, and we have a list of order items
# every item in this list is a tuple, product name followed by the price
items = [("Product1", 10), ("Product2", 20), ("Product3", 30)]
items.sort()
print(items)


# nothing is sorted or changed above because python does not know how to sort it
# in this case we need to define a function that python will use for sorting this list
def sort_function(item):
    # lets say we want to sort each item based on their price
    return item[1]


# when python attempts to sort this list, it gets each item and it will pass each item to our sort function
items.sort(key=sort_function)
print(items)


# lambdas
# the method we showed above is a bit messy and there is a better way to do this using lambdas.
# it is a simple one line function that we can pass to other function
# so we can write it as
# items.sort(key=lambda parameters: expression)
# in this case it will be
# items.sort(key=lambda item: item[1])
# this way we do not have to write the expression


## Map Function
items = [("Product1", 10), ("Product2", 20), ("Product3", 30)]

# imagine we want to transform this list into a different shape
# lets say we want to just have the prices of each item
# prices = []
# for item in items:
#     prices.append(item[1 ])

# so this map function will iterate over this iterable (items)
# and it will call this lambda function(item: itme[1])over each item of this iterable
x = map(lambda item: item[1], items)
for item in x:
    print(item)

# we cna also conver this from a map object into a list object
# prices = list(map(lambda item: item[1], items))
# print(prices)


## filter function
items = [("Product1", 10), ("Product2", 9), ("Product3", 12)]
# lets say we want to filter this list and get only the items that have a price greater than or equal to 10
# so we cna use the inbuilt filter function, which takes 2 arguments, a function and an iterable.
# item[1] >= 10, items returns a boolean value
x = filter(lambda item: item[1] >= 10, items)
# if we print  x = filter(lambda item: item[1] >= 10, items), we get a filter object,
# which is iterable, so we can loop over it and we can alsod convert it into a list right away
# print(x)

filtered_list = list(filter(lambda item: item[1] >= 10, items))
print(filtered_list)

## list comprehension
items = [("Product1", 10), ("Product2", 9), ("Product3", 12)]

prices = list(map(lambda item: item[1], items))
# we are iterating over each item in the iterable and then we are applying this expresiion
# [expression for item in items]
prices = [item[1] for item in items]

filtered_list = list(filter(lambda item: item[1] >= 10, items))
filtered_list = [item for item in items if item[1] >= 10]


## Zip function
list1 = [1, 2, 3]
list2 = [10, 20, 30]

# lets say we want to combine these 2 lists into a single list of  tuples like this
# [(1, 10), (2, 20), (3, 30)]
# we cant use a map function or list comprehension becaus eboth of hese work with a single list
# but here we are combining multiple lists, and therefore we will use the built in zip function
# which takes in multiple iterables
# it will returna zip object which is iterable, so we will use a list funciton
print(list(zip(list1, list2)))
# since zip takes in multiple iterables we can also pass in a string like
print(list(zip("abc", list1, list2)))
