import string

# ----------------------------------------------------------------------------------------------------------------------
# ------------------------------------------- ITERATOR PROTOCOL --------------------------------------------------------
# Iterator protocol: it consists of two methods:
#   a) __iter__ - this method returns an iterator
#   b) __next__ - method used to iterate over consecutive elements
#


class MyIteratorClass(object):

    def __init__(self, min_val, max_val, delta):
        self.cur_val = min_val              # current value - status tracker
        self.max_val = max_val
        self.step = delta

    def __iter__(self):
        """
        This method should return and iterator, so it is returning an
        instance of an object of class MyIteratorClass itself
        :return: the object itself
        """
        return self

    def __next__(self):
        """
        This function provides functionality returning next element from the iterator
        :return: next value
        """
        if self.cur_val <= self.max_val:
            self.cur_val += self.step
            return self.cur_val - self.step
        else:
            raise StopIteration


if __name__ == "__main__":
    mic1 = MyIteratorClass(min_val=1123.22, max_val=123423443, delta=32312)
    print(mic1)
    print(type(mic1))
    miciter1 = mic1.__iter__()
    print(miciter1)
    print(type(miciter1))
    for el in mic1:
        print(el)
