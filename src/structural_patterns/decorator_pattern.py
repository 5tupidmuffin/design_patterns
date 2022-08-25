#!/usr/bin/env python3

"""
    Theory: https://www.youtube.com/watch?v=GCraGHx6gso&list=PLrhzvIcii6GNjpARdnO4ueTUAVR9eMBpc&index=3
            https://www.dofactory.com/net/decorator-design-pattern
    SOLID Principles: https://en.wikipedia.org/wiki/SOLID
    Python Decorators: https://www.programiz.com/python-programming/decorator
"""


from abc import ABC, abstractmethod


# interface
class Beverage(ABC):
    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def get_cost(self) -> int:
        pass


# concrete beverage implementations
class Decaf(Beverage):
    def get_description(self) -> str:
        return "this beverage contains: Decaf"

    def get_cost(self) -> int:
        return 20


class Espresso(Beverage):
    def get_description(self) -> str:
        return "this beverage contains: Expresso"

    def get_cost(self) -> int:
        return 15


# decorator interface
class CondamentDecorator(Beverage):
    @abstractmethod
    def __init__(self, beverage: Beverage):
        pass

    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def get_cost(self) -> int:
        pass


# concrete decorator implementations
class CaramelDecorator(CondamentDecorator):
    beverage: Beverage
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def get_description(self) -> str:
        return self.beverage.get_description() + " + " + "Caramel"

    def get_cost(self) -> int:
        return self.beverage.get_cost() + 7


class SoyDecorator(CondamentDecorator):
    beverage: Beverage
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def get_description(self) -> str:
        return self.beverage.get_description() + " + " + "Soy"

    def get_cost(self) -> int:
        return self.beverage.get_cost() + 4


if __name__ == "__main__":
    # create an espresso
    espresso = Espresso()

    # add caramel
    caramel_espresso = CaramelDecorator(espresso)
    print("cost for Caramel Espresso: ", caramel_espresso.get_cost())

    # add soy
    soy_caramel_espresso = SoyDecorator(caramel_espresso)
    print("cost for Soy Caramel Espresso: ", soy_caramel_espresso.get_cost())

    print()

    # in a single line
    decaf_with_caramel = CaramelDecorator(Decaf())
    print(decaf_with_caramel.get_description())
    print("cost for Caramel Decaf: ", decaf_with_caramel.get_cost())


    """ 
    output:
    cost for Caramel Espresso:  22
    cost for Soy Caramel Espresso:  26

    this beverage contains: Decaf + Caramel
    cost for Caramel Decaf:  27
    """
