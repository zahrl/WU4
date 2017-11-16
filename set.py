numbers1 = set([1, 1, 2, 3, 5]) # set = unordered collection of unique elements

# Python doc: The sets module provides classes for constructing and manipulating unordered collections of unique elements. Common uses include membership testing, removing duplicates from a sequence, and computing standard math operations on sets such as intersection, union, difference, and symmetric difference.
# Like other collections, sets support x in set, len(set), and for x in set. Being an unordered collection, sets do not record element position or order of insertion. Accordingly, sets do not support indexing, slicing, or other sequence-like behavior.

numbers2 = {1, 3}

print(numbers1) # outputs {1, 2, 3, 5}

if numbers2.issubset(numbers1):
	print("numbers2 is a subset")

if numbers1.issuperset(numbers2):
	print("numbers1 is a superset")

set1 = numbers1
set2 = numbers2
set3 = set1 & set2 # intersection
set4 = set1 | set2 # union
set5 = set1 - set2 # difference

print(set3)
print(set4)
print(set5)