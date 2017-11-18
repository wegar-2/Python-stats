import abc # the module necessary to create abstract base class


# ----------------------------------------------------------------------------------------------------------------------
# 1. Create an abstract class
class GeneralFinancialInstrument(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        print("Class GeneralFinancialInstrument constructor called! ")

    @abc.abstractmethod
    def calculate_fair_value(self):
        """
        This function should contain implementation of function calculating
        the fair value of this instrument
        """
        pass

    @abc.abstractmethod
    def calculate_value_at_risk(self):
        """
        Implementations of this method in children classes should produce
        VaR values for this instrument
        """
        pass


# ----------------------------------------------------------------------------------------------------------------------
# 2. Create a child class of an abstract class: using subclassing
class StockOption(GeneralFinancialInstrument):

    def __init__(self):
        super().__init__() # calling the constructor of the parent class
        print("Constructor of class StockOption called. ")

    # Implementations of abstract class methods below
    def calculate_fair_value(self):
        print("Method calculate_fair_value of StockOption class called. ")

    def calculate_value_at_risk(self):
        print("Method calculate_value_at_risk of StockOption class called. ")

