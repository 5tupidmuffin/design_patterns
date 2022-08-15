#!/usr/bin/env python3

"""
    Theory: https://www.youtube.com/watch?v=v9ejT8FO-7I&list=PLrhzvIcii6GNjpARdnO4ueTUAVR9eMBpc&index=1
            https://www.dofactory.com/net/strategy-design-pattern
            https://sourcemaking.com/design_patterns/strategy
            https://en.wikipedia.org/wiki/Strategy_pattern
    OOP Composition: https://stackify.com/oop-concepts-composition/
    Python Implementation: https://www.youtube.com/watch?v=WQ8bNdxREHU
    Interfaces in Python: https://www.godaddy.com/engineering/2018/12/20/python-metaclasses/
"""

from abc import ABC, abstractmethod


# intefaces
class IQuackBehaviour(ABC):
    @abstractmethod
    def quack():
        pass


class IFlyBehaviour(ABC):
    @abstractmethod
    def fly():
        pass


# actual strategies
class NormalQuackStrategy(IQuackBehaviour):
    def quack(self):
        print("normal quack quack")


class ArtificialQuackStrategy(IQuackBehaviour):
    def quack(self):
        print("artificial quack quack")


class NormalFlyStrategy(IFlyBehaviour):
    def fly(self):
        print("normal fly")


class NoFlyStrategy(IFlyBehaviour):
    def fly(self):
        print("I cant fly :(")


# client
class Duck:
    quack_strat: IQuackBehaviour
    fly_strat: IFlyBehaviour
    def __init__(self, quackStrategy: IQuackBehaviour, flyStrategy: IFlyBehaviour):
        self.quack_strat = quackStrategy
        self.fly_strat = flyStrategy
    
    def quack(self):
        self.quack_strat.quack()
    
    def fly(self):
        self.fly_strat.fly()


if __name__ == "__main__":
    # changing stategies to create desired duck
    wild_duck = Duck(NormalQuackStrategy(), NormalFlyStrategy())
    rubber_duck = Duck(ArtificialQuackStrategy(), NoFlyStrategy())

    wild_duck.quack()
    wild_duck.fly()

    rubber_duck.quack()
    rubber_duck.fly()

    '''
    output:
    normal quack quack
    normal fly
    artificial quack quack
    I cant fly :(
    '''

