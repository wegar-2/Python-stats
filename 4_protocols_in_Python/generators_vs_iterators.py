# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ------------------------------------------  GENERATORS AND ITERATORS  ------------------------------------------------
# This script deals with the issue of generators and discusses similarities and differences between generators
# and iterators.
# ----------------------------------------------------------------------------------------------------------------------
#

# ----------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------   GENERATORS   -----------------------------------------------------
# Generators arise as:
#   1) function generators
#   2) generator classes
# These are discussed below.


# Ad. 1) function generators
def simple_function_generator(start, end, step):
    status = start
    while status <= end:
        yield status
        status += step


if __name__ == "__main__":
    for num, el in enumerate(simple_function_generator(start=1, end=13, step=1.345)):
        print(str(num) + ": " + str(el))
    # note:
    print("__next__" in dir(simple_function_generator(start=1, end=13, step=1.345)))


# Ad. 2) generator classes
class SimpleGeneratorClass(object):

    def __init__(self):
        pass

# ----------------------------------------------------------------------------------------------------------------------

