#!/usr/bin/env python3

""" 
    theory: https://www.youtube.com/watch?v=hUE_j6q0LTQ&list=PLrhzvIcii6GNjpARdnO4ueTUAVR9eMBpc&index=6
            https://www.dofactory.com/net/singleton-design-pattern
            https://en.wikipedia.org/wiki/Singleton_pattern
            https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
            https://www.geeksforgeeks.org/__new__-in-python/

            SINGLETON BAD
            https://en.wikipedia.org/wiki/Singleton_pattern#Criticism
            https://stackoverflow.com/questions/137975/what-are-drawbacks-or-disadvantages-of-singleton-pattern
"""


# implementation from https://en.wikipedia.org/wiki/Singleton_pattern#Python
class Singleton:
    __instance = None
    def __new__(cls, *args):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls, *args)
        return cls.__instance


class NonSingleton:
    def __init__(self):
        pass


if __name__ == "__main__":
    only_instance = Singleton()
    another_instance = Singleton()
    assert only_instance == another_instance
    # no AssertionError should be raised proving they point to the same instance


    first_nonsingleton = NonSingleton()
    second_nonsingleton = NonSingleton()
    assert first_nonsingleton == second_nonsingleton, "Two Different Instances!"
    # AssertionError will be raised since they point to two different instances


    """
    output:
    Traceback (most recent call last):
        File "./singleton_pattern.py", line 39, in <module>
            assert first_nonsingleton == second_nonsingleton, "Two Different Instances!"
    AssertionError: Two Different Instances!
    """
