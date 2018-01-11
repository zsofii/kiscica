# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod


class Allat(ABC):
    @abstractmethod
    def __init__(self):
        pass

    def __repr__(self):
        return "{} ({})".format(self.nev, type(self).__name__)

    @classmethod
    def fajnev(cls):
        return cls.__name__


class Macska(Allat):
    def __init__(self, nev):
        super(Macska, self).__init__()
        self.nev = nev


class Kutya(Allat):
    def __init__(self, nev):
        super(Kutya, self).__init__()
        self.nev = nev 
