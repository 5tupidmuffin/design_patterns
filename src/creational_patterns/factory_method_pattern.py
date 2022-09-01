#!/usr/bin/env python3

"""
    theory: https://www.youtube.com/watch?v=EcFVTgRHJLM&list=PLrhzvIcii6GNjpARdnO4ueTUAVR9eMBpc&index=5
            https://www.dofactory.com/net/factory-method-design-pattern
            https://sourcemaking.com/design_patterns/factory_method
"""


from abc import ABC, abstractmethod
import random
import sys
from typing import List


# interface for Animal
class Animal(ABC):
    pass


# concrete animal classes
class Dog(Animal):
    instance_count: int = 0
    def __init__(self):
        Dog.instance_count += 1


class Cat(Animal):
    instance_count: int = 0
    def __init__(self):
        Cat.instance_count += 1


class Mouse(Animal):
    instance_count: int = 0
    def __init__(self):
        Mouse.instance_count += 1


# interface factory classes
class AnimalFactory(ABC):
    @staticmethod
    @abstractmethod
    def create() -> Animal:
        pass


# concrete factory classes
class RandomAnimalFactory(AnimalFactory):
    animal_classes: List[Animal] = [Dog, Cat, Mouse]
    @staticmethod
    def create() -> Animal:
        randomly_selected_animal = random.choice(RandomAnimalFactory.animal_classes)
        return randomly_selected_animal()


class BalancedAnimalFactory(AnimalFactory):
    animal_classes: List[Animal] = [Dog, Cat, Mouse]
    @staticmethod
    def create() -> Animal:
        low_count_animal_class: Animal = None
        low_count = sys.maxsize
        for animal_class in BalancedAnimalFactory.animal_classes:
            if animal_class.instance_count < low_count:
                low_count_animal_class = animal_class
                low_count = animal_class.instance_count

        return low_count_animal_class()


if __name__ == "__main__":
    # will instatiate random animal class everytime
    random_animal = RandomAnimalFactory.create()
    print(type(random_animal))

    # will try to keep every animal class instance count equal
    balanced_animal = BalancedAnimalFactory.create()
    print(type(balanced_animal))

    another_balanced_animal = BalancedAnimalFactory.create()
    print(type(another_balanced_animal))


    '''
    output:
    <class '__main__.Cat'>
    <class '__main__.Dog'>
    <class '__main__.Mouse'>
    '''
