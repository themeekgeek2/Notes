'''
Built-in data structures in python include Tuples, Dictionaries and Sets
'''

tuple_a=(1,2,3,4) # This is a tuple

'''
Tuples are immutable (values are constant); Lists are mutable (can change later)

Lists can become tuples; Tuples can become lists

'''

list_a=[1,2,3,4]
tuple_b=tuple(list_a) # creating another tuple
type(tuple_b) # will return '<class 'tuple'>'

list_b=list(tuple_b) # turns the tuple back into a list
type(list_b) # returns <class 'list'>

'''
To work around the immutability of a tuple, you can replace the content of a tuple via assignment statement
'''

tuple_c=(1,2,3)
tuple_d=(8,9)

tuple_c=tuple_c.__add__(tuple_d) # returns '(1,2,3,8,9'; use EM DASH

'''
Dictionaries are a collection where information is stored in pairs of a unique key and the value associated with it.

Each key must be unique, otherwise Python will remove the first pair and keep the second

Dictionaries are mutable though you CANNOT change the key by itself

Keys can be strings, numbers or tuples that hold immutable objects

To retrieve a value, use its associated key in square brackets, preceded by the dictionary name

'''

my_dict={'Sam':67} # 'Sam' is the key; '67' is the key's value

dict_2={'mafu':67,'sora':62,'ura':72} # dictionaries can have multiple pairs
dict_2.keys() # The 'keys()' function lists all keys in a dictionary; returns 'dict_keys(['mafu','sora','ura'])
dict_2.values() # returns "dict_values([67,62,72,59])"

for i in dict_2.keys():
    print(i,dict_2[i]) # This loops through a dictionary and outputs its keys and key values

'''
Update() adds a new pair to a dictionary
'''

dict_2.update({'amatsuki':33})
# The input 'dict_2' will return "{'mafu':67,'sora':62,'ura':72,'amatsuki':33}"

'''
Pop() returns the value associated with the key and removes the pair
'''

dict_2.pop('ura')
# Returns '72' and removes ({'ura':72}) from the dictionary


