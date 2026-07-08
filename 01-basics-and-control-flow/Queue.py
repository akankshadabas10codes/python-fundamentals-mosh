# Queues
# FIFO - first in first out
# when we remove one item , we need to shift all other items to the left
# and shift all these items in memory
# therefore we can use a deque object instead
from collections import deque

queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)

# if we want to check if the queue is empty, we can do this
# because an empty list is considered false in python, therefore
# if the list is empty, the not operator will return true and the
# code block will be executed.
if not queue:
    print("empty queue")

## tuples
# a tuple is a read only list, we can use it to containa sequnce of ibejcyts but we cant modify it
# we use parenthesis or weihtout parenthesis to create a tuple
# if we have one item, we should add a trailing comma like 1,
# empty tupple is ()
# we can use * to rpeate the tuple
point = (1, 2) + (3, 4)
print(point)
point = (1, 2) * 3
print(point)
# we cna convert a list to a tuple by using the tuple keyword
# and since it is iterable we can also put a string
point = tuple([1, 2])
print(point)

# similar to
point = (1, 2, 3)
print(point[0])
print(point[0:2])
x, y, z = point
if 10 in point:
    print("exists")


## Swapping variables
x = 10
y = 11

z = x
x = y
y = z

print("x", x)
print("y", y)


# instead we can do
x, y = y, x
# x, y = 10, 11
# its like assigning a tuple on the LHS and then unpacking it on the RHS


## Arrays
# take less memory and perform faster, only when delaing with a large list of number
from array import array

# typecode is a string that determines the type of objects in the list
numbers = array("i", [1, 2, 3])
# we can invoke methods
# we can use .append, .insert, .pop, .remove
# every obejct in ths array should be of the same type
# we can't do numbers[0] = 1.0 in an array for integers
numbers[0]

## Sets
# a collection with no duplicates
numbers = [1, 1, 2, 3, 4]
# uniques = set(numbers)
# print(uniques)
# we use curly braces like {} to define a set
first = set(numbers)
second = {1, 5}
# we can add new items to the set or remove the existing ones
# second.add(5)
# second.remove(5)
# len(second)
# print(uniques)


# union of 2 sets
# this operator gives another set that includes the elements in all
# of the first and second sets
print(first | second)
# in this case we get {1, 2, 3, 4, 5}

# intersection of 2 sets
# returns a new set of a number/(s) that exists in both sets
print(first & second)
# {1}

# diff between 2 sets
print(first - second)
# we get a new set of the numbers {2, 3, 4}
# this set represents the elements that are unique to 1 set

# symmetric difference
# this returns items that are either in the first/ second set but not both
print(first ^ second)
# in this case {2, 3, 4, 5}

# unlike lists, the items in set are not in sequence, so we cant get their index
# we either use these operations above or we can check for the existence of an item in the set

if 1 in first:
    print("yes")


# to recap, set is an unordered collection of unique items, we cannot have duplicatres and this
# object are unordered, they are not in sequence, so we cannot access the using an index.

## Dictionaries
# a collection of key value pairs
# we use it to map a key to a value
# a real world example of this is a phone book where we map a person's name to their contact details.
# so we use the person's name as the key and their contatc information as the value
# for the key we can only use immutable types, so quite often we use integers. Whereas for the value
# we can use almost any data type.
# point = {"x": 1, "y": 2}
# we can also use the dict() function just like we have the list(), set(), tuple()
point = dict(x=1, y=2)
# we cna get the value associated with the key using an index
# thats why we do this
point["x"]
# note that oru index is the name of a key. because dictionaries are collections of key value pairs, we cannot
# access an item using a numeric index as we do with lists.
print(point["x"])
# we can also change the value
point["x"] = 10
# we can add a new key
point["z"] = 20
print(point)

# when reading a value, if we used an invalid key, we get an error
# for instance
# print(point["a"]) returns an error
# there are 2 workarounds here
# one solution is to check  for the existence of the key
if "a" in point:
    # then we will get the vlaue of the item with a key "a" and then print it
    print(point["a"])

# the other solution is the use the "get" method
# if the key doesn't exist, it by default returns none, or we can pass default value as a second argument
print(point.get("a", 0))
# to delete a item we use a del statement
del point["x"]
print(point)

# looping over a dictionary defaults over looping over the keys only
for x in point:
    print(x)

# in this example the var is still the key
# and the point[key] returns the value corresponding to that key.
for key in point:
    print(key, point[key])

# there is another way to iterate over a dictionary
# point.items() gives all the key - value pairs
for x in point.items():
    print(x)

# in each iteration we get a tuple with the key and value
# and we can unpack it here in the for loop itself

for key, value in point.items():
    print(key, value)

# point.items() gives us each key-value pair in the dictionary.
# Each pair is returned as a tuple, like ("x", 10).
# We can store the whole tuple in one variable.
# Or we can unpack the tuple into key and value directly.


## Dictionary comprehensions
# what this code is doing, is that we have an empty "values" list,
# for x in a range, we multiply the number by 2 and then we are adding
# it in the values list
# values = []
# for x in range(5):
#     values.append(x * 2)

# we can either use a map funciton or a list comprehension
# list comprehension
# [expression for item in items]
# values = {x * 2 for x in range(5)}
# print(values)

# dictionary comprehension
values = {x: x * 2 for x in range(5)}
print(values)

# tuples version
# values = (x * 2 for x in range(5))
# print(value)
# but we get a generator when we run this


## unpacking operator
numbers = [1, 2, 3]
print(numbers)
print(1, 2, 3)
# to get the above
# here we unpack a container, take out its individual elements and then pass them as arbitrary arguments
print(*numbers)

# recreating lists
valuesx = list(range(5))
valuesx = [*range(5), *"Hello"]
print(valuesx)

first = [1, 2]
second = [3]
# now to unpack this lsit we cna do this
valuesagain = [*first, "a", *second]
print(valuesagain)

# in dictionary as well
first = {"x": 1}
second = {"x": 10, "y": 2}
combines = {**first, **second, "z": 1}
print(combines)


## exercise
# write a program to find the most repeated character in this text
# we need ot know how many times each char is repeated
# we use a dictionary
from pprint import pprint

sentence = "This is a common interview questions"
char_frequencey = {}
for char in sentence:
    if char in char_frequencey:
        char_frequencey[char] += 1
    else:
        char_frequencey[char] = 1
pprint(char_frequencey, width=1)

## sort the dict by freq of chars
# but we cant sort them, take them out convert it to a tuple, pt it in a list and then sort it
# rmb that .items() returns all the key value pairs
char_frequencey_sorted = sorted(
    char_frequencey.items(), key=lambda kv: kv[1], reverse=True
)
print(char_frequencey_sorted[0])
