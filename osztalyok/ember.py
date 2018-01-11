# -*- coding: utf-8 -*-
from datetime import datetime


class Ember:
    def __init__(self, nev, szuletesi_datum, anyja_neve, hazi_allatok=None):
        if nev is not None and szuletesi_datum is not None and anyja_neve is not None:
            self.nev = nev
            self.szuletesi_datum = datetime.strptime(szuletesi_datum, "%Y.%M.%d.").date()
            self.anyja_neve = anyja_neve
            self.hazastars = None
            if hazi_allatok is not None:
                self.hazi_allatok = hazi_allatok
            else:
                self.hazi_allatok = []
        else:
            raise ValueError("A mezők kitöltése kötelező!")

    def __repr__(self):
        return self.nev

    @staticmethod
    def kromoszoma_szam():
        return 46

    def __add__(self, other):
        self.hazasodik(other)

    def __sub__(self, other):
        self.elvalik(other)

    def hazasodik(self, hazastars):
        if self.hazastars is None:
            if type(hazastars) is Ember:
                if hazastars.eletkor() >= 18:
                    self.hazastars = hazastars
                    hazastars.hazastars = self
                    print("{} összeházasodott {} -val/vel!".format(self, hazastars))
                else:
                    print("{} nem hazasodhat, mert kiskoru ({} éves)".format(hazastars, hazastars.eletkor()))
            else:
                raise TypeError("A házastárs nem ember!")
        else:
            print("{} mar nem hazasodhat, van mar hazastarsa!".format(self))

    def eletkor(self):
        return datetime.now().date().year - self.szuletesi_datum.year

    def elvalik(self, hazastars):
        if self.hazastars is hazastars:
            self.hazastars = None
            hazastars.hazastars = None
            print("{} es {} elvaltak egymastol".format(self, hazastars))
        else:
            print("{} es {} nem hazasodtak ossze, nem valhatnak el".format(self, hazastars))
