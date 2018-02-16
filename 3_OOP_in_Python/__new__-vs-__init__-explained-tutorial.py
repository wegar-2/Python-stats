# -------------------------------------------------------------------------------------------------------------------- #
# ------- This script is a walk through an excellent article: http://spyhce.com/blog/understanding-new-and-init  ----- #
# -------------------------------------------------------------------------------------------------------------------- #
# Note: only new-style classes are dealt with here

# High level view of the difference between __new__ and __init__ methods:
#   1) __new__ - this method handles object creation
#   2) __init__ - this method handles object initialization
#


class SampleClassOne(object):

    def __new__(cls):
        """

        :return: returns result of the call of __new__ method
        """
        print("Class SampleClass __new__ method has been called...")
        return super(SampleClassOne, cls).__new__(cls)

    def __init__(self):
        """
        This method is dealing with the object initalization
        """
        print("Class SampleClass __init__ method has been called...")


if __name__ == "__main__":
    obj1 = SampleClassOne()

# Note that inside the __new__ method constructor is parent class constructor is called using the syntax
# super(MyClass, cls).__new__(cls)
#
# --------------------------------------------------
# How are the __new__ and __init__ methods executed?
#
# 1.
# First of all note that the __new__ method is executed first. The __new__ method is actually executed automatically
# when calling the class name [i.e. when SampleClassOne() appears in your code]
#
# 2.
# Secondly it should be noted that the __init__ method is called every time the instance of the SampleClassOne is
# returned by __new__. Moreover, when an instance of class SampleClassOne is returned by __new__ method, it is
# automatically passed to the __init__ function!!!
#
#
# For comparison, have a look at the code below in which the __new__ method does NOT return an instance of the class





