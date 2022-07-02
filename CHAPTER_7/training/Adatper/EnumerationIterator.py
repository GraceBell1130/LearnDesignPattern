from Enumeration import Enumeration
from Iterator import Iterator

class EnumerationIterator(Iterator):
    def __init__(self, enumeration: Enumeration) -> None:
        self.enumeration: Enumeration = enumeration

    def hasNext(self):
        self.enumeration.hasMoreElements()

    def next(self):
        self.enumeration.nextElement()

    def remove(self):
        pass