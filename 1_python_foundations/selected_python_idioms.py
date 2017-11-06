import string
import numpy as np
import itertools

# 1. how to elegantly iterate over a list with iteration number
my_list = list(string.ascii_lowercase[0:10])
for iter_num, iter_item in enumerate(my_list):
    print(iter_num, ": ", iter_item)

# 2. how to elegantly iterate over Python's dictionary
my_sample = list(set(np.random.randint(low=1, high=len(string.ascii_lowercase), size=20)))
my_letters = [list(string.ascii_lowercase)[el] for el in my_sample]
my_dict = dict(zip(my_sample, my_letters))
for iter_key, iter_item in my_dict.items():
    print(iter_key, ": ", iter_item)

# some more on Python's dictionaries
print(list(my_dict)) # list of dictionary keys
print(list(my_dict.keys())) # list of dictionary keys
print(list(my_dict.values())) # list of dictionary values
print(list(my_dict.items())) # list of tuples that are (key, value) pairs

# 3. Joining strings
# 3.1. First, the wrong way
list_of_strings = ["THIS", "IS", "SPARTAAAA", "!!!!!!"]
leonidas_quote = ""
for word in list_of_strings:
    leonidas_quote += " "
    leonidas_quote += word
print(leonidas_quote)
# 3.2. Now, the elegant way
leonidas_quote = " ".join(list_of_strings)
print(leonidas_quote)

# 4. cartesian product in Python: library itertools needed
# 4.1. cartesian product of sets
set1 = {"a", "b", "q", "w", "u", "d"}
set2 = {2, 5, 4, 78}
set1_x_set2 = list(itertools.product(set1, set2)) # note that order of the input structures is not retained
# 4.2. cartesian product of two lists
list1 = [1, 2, 3, 4, 5]
list2 = ["a", "c", "v"]
list1_x_list2 = list(itertools.product(list1, list2)) # order is retained
# Sidenote: itertools.product() accepts iterables as its argument
# Iterable - class that has method __iter__ defined
# Iterator - class that has method __next__ defined

# 5. Initializing a dictionary's entries
# 5.1. first example
group1 = ["a", "b", "c"]
group2 = [3, 6, 10]
group3 = [22, 2]
list_of_tuples = list(itertools.product(group1, group2, group3))

my_dict_2 = {} # empty dictionary; sidenote: set1 = set() to produce an empty dictionary
for (el1, el2, el3) in list_of_tuples:
    # iterating over a list of tuple
    my_dict_2[el1] = my_dict_2.get(el1, 0) + el2*el3
# 5.2. second example
group1 = ["a", "b"]
group2 = [4, 5]
group3 = [1, 2]
list_of_tuples = list(itertools.product(group1, group2, group3))
test_dict = {}
for (el1, el2, el3) in list_of_tuples:
    test_dict[el1] = test_dict.get(el1, 0) + el2*el3
    
