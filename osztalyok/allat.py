# -*- coding: utf-8 -*-


class Allat:
    def __init__(self, nev):
        self.nev = nev

    def __repr__(self):
        return "{} ({})".format(self.nev, type(self))


class Macska(Allat):
    def __init__(self, nev):
        super(Macska, self).__init__(nev)
