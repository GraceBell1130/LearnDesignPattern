from pytest import *
from Singleton import *

def test_Singletone():
    a = Singleton()
    b = Singleton()
    assert a is b


def test_SingletoneLazy():
    a = SingletonLazy.getInstace()
    b = SingletonLazy.getInstace()
    assert a is b
