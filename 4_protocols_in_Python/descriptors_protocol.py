#######################################################################
##### Based on: https://docs.python.org/3.6/howto/descriptor.html #####
#######################################################################


###############################
##### DESCRIPTORS: HOW TO #####
###############################

### Descriptor: definition
### Descriptor - any object whose attribute access has been overridden by methods in
###              the descriptor protocol. Those methods are:
###              1) __get__()
###              2) __set__()
###              3) __delete__()

# descr.__get__(self, obj, type=None) --> value
# descr.__set__(self, obj, value) --> None
# descr.__delete__(self, obj) --> None

# Some other methods used here:

# 1. getattr()
# getattr(object, name[, default]) -> value
# Get a named attribute from an object; getattr(x, 'y') is equivalent to x.y.
# When a default argument is given, it is returned when the attribute doesn't
# exist; without it, an exception is raised in that case.
# Type:      builtin_function_or_method

# 2. setattr()
# Signature: setattr(obj, name, value, /)
# Docstring:
# Sets the named attribute on the given object to the specified value.
# setattr(x, 'y', v) is equivalent to ``x.y = v''
# Type:      builtin_function_or_method

# 3. __get__() method
# object. __get__(self, instance, owner)
# self - required. Instance of the class, passed automatically on call.
# instance - required. Instance is the instance that the attribute was accessed through,
# or None when the attribute is accessed through the owner.
# owner - required. Owner is always the owner class.

class MyClass(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y


obj1 = MyClass(1, 3)
obj2 = MyClass(2, 33)

obj1.__getattribute__(name="x")


# ----- Example of a descriptor class
class TypedProperty(object):

    # constructor
    def __init__(self, name, type, default=None):
        self.name = name
        self.type = type
        self.default = default if default else type()

    def __get__(self, instance, cls):
        return getattr(instance, self.name, self.default)


# ----- Another example
class MyTestClass(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        print("Constructor of MyTestClass has been called. ")

    def print_member_variables(self):
        print("x: ", self.x)
        print("y: ", self.y)


class MyTestChildClass(MyTestClass):

    def __init__(self, x, y, z):
        super().__init__(x=x, y=y)
        self.z = z
        print("Class MyTestChildClass constructor has been called. ")

    def print_member_variables(self):
        print("z: ", self.z)


# --- Have a look at __dict__ of a custom class object
obj1 = MyTestClass(x=12, y=32)
obj1.print_member_variables()
print(obj1.__dict__)
obj2 = MyTestChildClass(x=123, y=32, z=333)
print(obj2.print_member_variables())


class DescriptorClass(object):

    def __init__(self, x):
        self.x = x

    def __get__(self, instance, owner):
        print("Returning value of x member of a class DescriptorClass instance. ")
        print("owner argument: ", owner)
        print("instance argument: ", instance)
        return self.x


obj3 = DescriptorClass(x=12)
obj3.x