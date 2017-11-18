###########################################################################
# A walk through the "Python 3 OOP Part 5 - Metaclasses"                  #
# article from http://blog.thedigitalcatonline.com/blog/2014/09/01/       #
# python-3-oop-part-5-metaclasses/                                        #
# by Leonardo Giordani                                                    #
###########################################################################

x = int(123)
print(type(x))
print(x.__class__) # int
print(x.__class__.__bases__) # parent class of int is object

# NOTE: In Python, everything inherits from the "object"
print(object.__bases__) # returns an empty tuple (). Therefore, there is nothing above object in Python's class
# hierarchy

type(object) # returns "type". "Type" is class that is instanced to get classes, e.g.:
type(int) # returns "type"

# Metaclasses: when a class inheriting from "type" class is defined, other newly created classes can be instructed to
#  treat it as their metaclass instead of the default "type"


# an example of a metaclass
class SingletonMetaclass(type):
    # by default class_instance is None
    class_instance = None

    def __call__(cls, *args, **kwargs):
        if cls.class_instance is None:
            cls.instance = super(SingletonMetaclass, cls).__call__(*args, **kwargs)
        return cls.class_instance



class MyClass(object):

    def __new__(cls, *args, **kwargs):
        pass

    def