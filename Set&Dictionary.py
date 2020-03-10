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