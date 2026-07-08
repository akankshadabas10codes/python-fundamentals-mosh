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
