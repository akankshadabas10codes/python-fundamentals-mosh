# Stacks
# LIFO - last in firstout - the last book you put on the stack is the first one you can take out.
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
# when the user presses back the last page should be removed from the stack
last = browsing_session.pop()
print(last)
print(browsing_session)
print("redirect", browsing_session[-1])
# if the stack is empty, we should disable the back button
# we do if not browsing_session to check if the stack is empty,
# because an empty list is considered false in python, therefore
# if the list is empty, the not operator will return true and the
# code block will be executed.
if not browsing_session:
    browsing_session[-1]
    print("disable back button")
