'''
Adding to a list
'''
myList=[5,'word',2.3,False]
print(myList[2])

'''
Print and/or manipulate any value
'''

cart=[]
cart.append(1342)
cart.append(2541)
print(cart)

'''
Returns a list of the functions in the built-in dir() module
'''

for n in dir(list):
    print(n)

# Built-in functions

'''
append() : adds to a list
copy() : makes a copy of a list
extend(): adds items from one list to the end of another list
    **note: you can also select from just a portion of a list to extend to another

pop() : retrieves and removes a list's last item
remove() : removes the first occurrence of the value in a parenthesis
clear() : removes all items from the list
count() : searches for a specific item in a list based on parameter value (what's in the parenthesis)
    **note: This feature is case-sensitive.

index() : returns the index of the first occurrence of a data item

'''

