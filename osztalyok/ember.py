# -*- coding: utf-8 -*-


class Ember:
    def __init__(self, nev, szuletesi_datum, eletkor, anyja_neve, hazi_allatok=None):
        if nev is not None and szuletesi_datum is not None and anyja_neve is not None:
            self.nev = nev
            self.szuletesi_datum = szuletesi_datum
            self.eletkor = eletkor
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

    def __add__(self, other):
        self.hazasodik(other)
        print("{} es {} hazasok".format(self, other))

    def __sub__(self, other):
        if self.hazastars is other:
            self.elvalik(other)
            print("{} es {} elvaltak".format(self, other))
        else:
            print("{} es {} nem hazasodtak ossze, nem valhatnak el".format(self, other))

    def hazasodik(self, hazastars):
        if self.hazastars is None:
            # TODO: leellenőrizni, hogy még nem házas-e!!
            if type(hazastars) is Ember:
                self.hazastars = hazastars
                hazastars.hazastars = self
                print("{} összeházasodott {} -val/vel!".format(self, hazastars))
            else:
                raise TypeError("A házastárs nem ember!")
            if self.eletkor < 18:
                print("{} nem hazasodhat, meg kiskoru".format(self))
        else:
            print("{} mar nem hazasodhat, van mar hazastarsa!".format(self))

    def elvalik(self, hazastars):
        if self.hazastars is not None:
            self.hazastars = None
            hazastars.hazastars = None
            print("{} es {} elvalatak egymastol".format(self, hazastars))
        else:
            print("{} nem is volt hazas, nem valhat el".format(self))
