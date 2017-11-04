# A guided tour based on http://anandology.com/python-practice-book/iterators.html and Python Turtorial:
# https://docs.python.org/3.6/tutorial/classes.html#iterators

import string

# 1.
# iterating over a list
for item in ["a", "aa", 1, 32, 12, "qwe"]:
    print(item)
# iterating over a string: prints its symbols
for item in "Kac-Feynman formula":
    print(item)
# iterating over the dictionary
for item in {1: "a", 2: "q", 3: "pp"}:
    print(item)

# 2. What is going under the hood in the examples above?
test_list = list(string.ascii_lowercase[0:4])
# iter() function takes an iterable object and returns an iterator
iter_test_list = iter(test_list) # iter_test_list is an iterator
print(iter_test_list.__next__()) # 'a'
print(iter_test_list.__next__()) # 'b'
print(iter_test_list.__next__()) # 'c'
print(iter_test_list.__next__()) # 'd'

# what happens when all elements of an iterator have been printed: StopIteration object error is raised:
test_list = list(string.ascii_lowercase[0:10])
iterator_test_list = iter(test_list)
while True:
    try:
        print(next(iterator_test_list))
    except StopIteration:
        print("StopIteration exception!")
        break


# Formally, what makes a class iterable is having implementation of __iter__() and __next__() methods
# Cf. the example below:
class MyIteratorClass:
    """
    This class is a test class that contains implementation of the iterator protocol, i.e. it has __iter__ and
    __next__ methods defined. The class, as an iterator, returns a fixed number of consecutive even, natural numbers
    """

    def __init__(self, n):
        """
        This is class contructor, it sets the maximum number of even numbers that can be returned
        :param n: maximum number of even numbers that can be returned by the iterator made from this class instance
        """
        self.iter_status = 0
        self.max_val = n

    def __iter__(self):
        """
        This is the implementation of the __iter__ method required by the iteration protocol.
        Here, it simply returns the object. It needs not be always the case, cf. below
        :return: itself
        """
        return self

    def __next__(self):
        """
        Implementation of the __next__ method of the iteration protocol
        :return:
        """
        if self.iter_status < self.max_val:
            self.iter_status += 1 # increment
            return (self.iter_status-1)*2
        else:
            raise StopIteration("StopIteration raised from the MyIteratorClass object!")


# test whether the class works as expected
test_obj = MyIteratorClass(n=10)
for item in test_obj:
    print(item)

