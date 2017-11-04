import string
import numpy as np

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
