#!/usr/bin/env python3

"""
    theory: https://www.youtube.com/watch?v=v-GiuMmsXj4&list=PLrhzvIcii6GNjpARdnO4ueTUAVR9eMBpc&index=5
            https://www.dofactory.com/net/abstract-factory-design-pattern
            https://sourcemaking.com/design_patterns/abstract_factory

            example implemented here is from https://www.dofactory.com/net/abstract-factory-design-pattern
"""


from abc import ABC, abstractmethod


# interfaces
class Harbivore(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass


class Carnivore(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def eats(self, prey: Harbivore):
        pass


class AnimalFactory(ABC):
    @abstractmethod
    def create_harbivore(self) -> Harbivore:
        pass

    @abstractmethod
    def create_carnivore(self) -> Carnivore:
        pass


class Habitat(ABC):
    @abstractmethod
    def __init__(self, animal_factory: AnimalFactory):
        pass

    @abstractmethod
    def run_food_chain(self):
        pass


# concrete implementations
# animals
class Deer(Harbivore):
    def __str__(self) -> str:
        return "Deer"


class Lion(Carnivore):
    def __str__(self) -> str:
        return "Lion"

    def eats(self, prey: Harbivore):
        print(f"{self} eats {prey}")


# i know tuna isnt harbivore
class Tuna(Harbivore):
    def __str__(self) -> str:
        return "Tuna"


class Shark(Carnivore):
    def __str__(self) -> str:
        return "Shark"

    def eats(self, prey: Harbivore):
        print(f"{self} eats {prey}")


# factories
class LandAnimalFactory(AnimalFactory):
    def create_harbivore(self) -> Harbivore:
        return Deer()

    def create_carnivore(self) -> Carnivore:
        return Lion()


class AquaticAnimalFactory(AnimalFactory):
    def create_harbivore(self) -> Harbivore:
        return Tuna()

    def create_carnivore(self) -> Carnivore:
        return Shark()


class World(Habitat):
    _harbivore: Harbivore
    _carnivore: Carnivore
    def __init__(self, animal_factory: AnimalFactory):
        self._harbivore = animal_factory.create_harbivore()
        self._carnivore = animal_factory.create_carnivore()

    def run_food_chain(self):
        self._carnivore.eats(self._harbivore)
        


if __name__ == "__main__":
    # for grassland habitat
    land_animal_factory = LandAnimalFactory()
    grassland_habitat = World(land_animal_factory)
    grassland_habitat.run_food_chain()

    # for aquatic habitat
    aquatic_animal_factory = AquaticAnimalFactory()
    ocean_habitat = World(aquatic_animal_factory)
    ocean_habitat.run_food_chain()


    """
    output:
    Lion eats Deer
    Shark eats Tuna
    """
