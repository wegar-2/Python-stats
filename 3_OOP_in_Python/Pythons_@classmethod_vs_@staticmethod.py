class SampleClass(object):

    # a static member variable
    static_member = []

    def __init__(self):
        print("Class SampleClass constructor has been called...")

    # the method below is used to set the value of the SampleClass class static member
    @classmethod
    def my_class_method(cls, x):
        print("Inside the my_class_method of SampleClass...")
        SampleClass.static_member = x

    # the method below is simply printing the value of SampleClass static member
    @staticmethod
    def my_static_method():
        print("Inside my_static_method...")
        print("SampleClass.static_member: ", SampleClass.static_member)


# have a look at how the stuff works
if __name__ == "__main__":
    obj1 = SampleClass()
    obj1.my_static_method()
    obj1.my_class_method(x=[1, 5, 4, 2, 1,])
    obj1.my_static_method()

