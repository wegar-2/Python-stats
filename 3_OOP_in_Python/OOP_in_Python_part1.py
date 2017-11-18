### Intro: A class in Python


class Car(object):

    def __init__(self):
        print("Class 'Car' constructor called. ")

    # a class method is made static by using the "@staticmethod" decorator
    @staticmethod
    def make_sound():
        print("Wrroooom!!!")


# make a class 'BigCar' that inherits from class 'Car'
class BigCar(Car):
    # define the class constructor
    def __init__(self):
        super().__init__()
        print("Class")

    # SIDENOTE on @staticmethod: transforms a function into a static method.
    # A static method does not receive an implicit first argument. It can be called on
    # both: class instances and on the class itself
    @staticmethod
    def make_loud_sound():
        print("Wrroooom, Wrroooom, Wrroooom!!!")


car1 = Car()
car1.make_sound()

bigCar = BigCar()
bigCar.make_sound() # call method of a parent class
bigCar.make_loud_sound() # call method of its own

# to finish with, check base (i.e. parent) classes
print(bigCar.__class__)
print(bigCar.__class__.__bases__) # class "Car"
print(car1.__class__)
print(car1.__class__.__bases__) # all classes inherit from "object"
type(car1.__class__) # get type of "Car" ===> "type"


###########################################################################
# A walk through the "Python 3 OOP Part 2 - Classes and members"          #
# article from http://blog.thedigitalcatonline.com/blog/2014/08/20/       #
# python-3-oop-part-2-classes-and-members/#.WeNxfnCxVjU                   #
# by Leonardo Giordani                                                    #
###########################################################################

##########################################
##### 1. Python Classes Strike Again #####
##########################################

x = 1
type(x) # int
type(type(x)) # type


# In Python, everything is an object, and so a class is an object as well
class Gun:

    def __init__(self, make, rifle_length, loaded):
        print("Class 'Gun' constructor called. ")
        self.make = make
        self.rifle_length = rifle_length
        self.loaded = loaded

    def shoot(self):
        if self.loaded:
            print("Boom!")
            self.loaded = False # need to load after you shoot
        else:
            print("Load the gun first!")

    def load(self):
        print("Loading the gun...")
        self.loaded = True


# create two guns
gun1 = Gun("PGZ", 35, True)
gun2 = Gun("PGZ", 70, False)

# Gun was declared without specifying parent class explicitly, check if it is "object"
print(Gun.__bases__) # O.K., it's "object"!
print(Gun.__class__) # "type", ofc

print("Memory address of gun1: " + hex(id(gun1)))
print("Memory address of gun2: " + hex(id(gun2)))

# address of the class is identical for both instances
print(hex(id(gun1.__class__)) == hex(id(gun2.__class__)))


# static attributes of a class: checking out how they work
class Car2:
    color = "red"

    def __init__(self, make):
        print("Class 'Car2' constructor called!")
        self.make = make


car2 = Car2(make="Porsche")
car3 = Car2(make="Mercedes")
Car2.color = "blue"

print("car2.color: ", car2.color)
print("car3.color: ", car3.color)


############################################
##### 2. Raiders of the Lost Attribute #####
############################################

### "__dict__" attribute of a Python's object
car2.__dict__
Car2.__dict__ # note, that the static attribute is listed here
gun1.__dict__

### What is seen here for class "Car2" is that the static attribute is not listed
### in the output from the "car2.__dict__"
try:
    print(car2.__dict__["color"]) # when only this line is run, KeyError returned
except Exception as exc:
    print(car2.__class__.__dict__["color"])

# objects' attributes are looked for by the magic function __getattribute__
print(car2.__getattribute__("color"))
print(gun1.__getattribute__("make"))


#####################################
##### 3. Revenge of the Methods #####
#####################################

### 3.1. "function" vs. "bound method" in Python
print(gun1.__dict__)
print(Gun.__dict__)

# shoot and load routine
print(gun1.loaded)
gun1.shoot()
print(gun1.loaded)
gun1.load()
print(gun1.loaded)

print(id(gun1.shoot) == id(Gun.shoot)) # False!
print(Gun.__dict__["shoot"]) # class "function" object returned
print(gun1.shoot) # class "bound method" object returned

gun1.shoot()
print(gun1.loaded)
Gun.load(gun1) # an alternative way to load a gun to gun1.load()
print(gun1.loaded)

### So: Gun.load(gun1) works identically to gun1.load()
### The question now is: how does the gun1.load() work under the hood?

gun1.__class__.__dict__["load"] # get the method from the class of object gun1
gun1.__class__.__dict__["load"].__get__(gun1) # use the __get__ method and pass gun1 object to it


#######################################
##### 4. When Methods Met Classes #####
#######################################

