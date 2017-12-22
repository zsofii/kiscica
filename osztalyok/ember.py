# -*- coding: utf-8 -*-


class Ember:
    def __init__(self, nev, szuletesi_datum, anyja_neve, hazi_allatok=None):
        if nev is not None and szuletesi_datum is not None and anyja_neve is not None:
            self.nev = nev
            self.szuletesi_datum = szuletesi_datum
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

    def hazasodik(self, hazastars):
        # TODO: leellenőrizni, hogy még nem házas-e!!
        if type(hazastars) is Ember:
            self.hazastars = hazastars
            hazastars.hazastars = self
            print("{} összeházasodott {} -val/vel!".format(self, hazastars))
        else:
            raise TypeError("A házastárs nem ember!")