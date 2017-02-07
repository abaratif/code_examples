
# Example usage of zip, map, reduce to combine two first name and last name lists, then reduce the combined array into a string
def combineTwoLists(first, second):
	zipped = zip(first, second)

	# print(zipped)
	# [('Dorky', 'Dorkerton'), ('Jimbo', 'Smith'), ('Jeff', 'Johnson')]

	# The list comprehension way
	# listComp = [x + " " + y for x, y in zipped]
	# print(list(listComp))
	# ['Dorky Dorkerton', 'Jimbo Smith', 'Jeff Johnson']

	# The Map way
	f = lambda a : a[0] + " " + a[1]
	listComp = map(f, zipped)




	f = lambda a,b: a + ", " + b
	result = reduce(f, listComp)

	# Dorky Dorkerton, Jimbo Smith, Jeff Johnson

	# print(type(result))
	# <type 'str'>

	return result

first = ['Dorky', 'Jimbo', 'Jeff']
second = ['Dorkerton', 'Smith', 'Johnson']

print(combineTwoLists(first, second))


