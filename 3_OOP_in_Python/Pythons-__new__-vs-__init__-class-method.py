# ---------------------------------------------------------------------------------------------------------------------
#
# ---------------------------------------------------------------------------------
# ------ High-level comparison of the __new__() and __init__() class methods ------
# ---------------------------------------------------------------------------------
#
#
# A) __new__()
#
# __new__() method: used to control the creation of a new instance of a class. The
# __new__() method is the first step in a class instance creation process. It is called
# first and it is responsible for returning a new instance of a class
#
#
# B) __init__()
#
# __init__() method: used to control the initialization of a new instance of a class.
# The member function __init__() does not return anything! it's only responsible for initialization
# once an instance has been created.
#
# The __new__() accepts a type as the first argument
#


class MyClass(object):

    def __new__(cls, *args, **kwargs):
        return super(MyClass).__

    def __init__(self, x):
        self.x = x


# ----------------------------------------------------------------------------------------------------------------------
# Sidenote: difference between __init__() method and __call__() method
class MyTestClass(object):

    def __init__(self):
        print("Method __init__() of MyTestClass called...")

    def __call__(self, *args, **kwargs):
        print("Method __call__() of class MyTestClass called...")


obj1 = MyTestClass() # __init__() called here
obj1() # __call__() called here

# ----------------------------------------------------------------------------------------------------------------------
# Sidenote to sidenote: *args and **kwargs in practice

