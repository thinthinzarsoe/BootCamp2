#Sets

Set&Dictionaries.py

set - {}

includes a data type for sets.
Curly braces or the set() function can be used to create sets.

basket = {'apple', 'orange', 'pear', 'orange', 'banana'}
print(basket)		# show that duplicates have been removed

'orange' in basket		# fast membership testing
'crabgrass' in basket

Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alazazam')
a 			# unique letters in a
a - b 		# letters in a but not in b
a | b 		# letters in a or b or both
a & b 		# letters in both a and b
a ^ b 		# letters in a or b but not both

a = {x for x in 'abracadabra' if x not in 'abc'}
a
# ANS: {'d', 'r'}

-----

fruits = {"apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"}
print("cherry" in fruits)

fruits.add("cucumber")
fruits
fruits.update("grape")
fruits
fruits.remove("banana")
fruits
fruits.discard("kiwi")
fruits
----------------
>>> Dictionaries

#Dictionaries

#Another useful data type built into Python is the dictionary

tel = {'jack': 4098, 'sape': 4139}
tel['sape']
tel['guido'] = 4127
tel

---------------

del tel['sape']
tel['irv'] = 4137
tel

list(tel) # change to list

sorted(student) # Alphabet Sorting

'MgOo' in student
'MaMa' not in student

---------------


dict(sape=4319, guido=4127, jack=4098)

{x: x**2 for x in (2, 4, 6)}

>>> for x in 2, 4, 6:
...     print(x, ':', x**2)
...
2 : 4
4 : 16
6 : 36

-------------
When looping through Dictionaries

knights = {'gallahad': 'the pure', 'robin': 'the brave', 'sape' : 4355}
for x, y in knights.items():
	print(x, y)

for x, y in enumerate(['tic', 'tac', 'toe']):
	print(x, y)

-------------

questions = ['name', 'quest', 'favourite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
	print('What is your {0}? It is {1}.'.format(q, a))

#Sum

questions = ['name', 'quest', 'favourite colour']
answers = ['lancelot', 'the holy grail', 'blue']
result = ['1', '2', '3']
for q, a, i in zip(questions, answers, result):
	print('What is your {0}? It is {1}. It is {2}'.format(q, a, i))

-------------

print('{0} and {1} , {2} and {3}'. format('spam', 'eggs', 'color', 'food'))

https://docs.python.org/3/tutorial/

==============================