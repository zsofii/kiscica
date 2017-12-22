# -*- coding: utf-8 -*-


class Ember(object):
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

    def hazasodik(self, hazastars):
        if type(hazastars) is Ember:
            self.hazastars = hazastars
            hazastars.hazastars = self
            print("{} összeházasodott {} -val/vel!".format(self, hazastars))
        else:
            raise TypeError("A házastárs nem ember!")


class Jarmu(object):
    def __init__(self, rendszam, szin, marka, evjarat, kapacitas=5):
        self.szin = szin
        self.marka = marka
        self.evjarat = evjarat
        self.kapacitas = kapacitas
        self.utasok = []
        self.rendszam = rendszam

    def utas_beszall(self, utas):
        if self.kapacitas > len(self.utasok):
            self.utasok.append(utas)
            print("Jelenleg {} utas tartozkódik a járműben!".format(len(self.utasok)))

    def utas_kiszall(self, utas):
        if utas in self.utasok:
            self.utasok.remove(utas)
        else:
            print("{} nincs a {} utasai között!".format(utas, self))

    def utas_lista(self):
        print("A {} jármű utasai: {}".format(self.szin, self.utasok))

    def __repr__(self):
        return self.rendszam


class Auto(Jarmu):
    def __init__(self, rendszam, szin, marka, evjarat, utas_kapacitas=4, csomag_kapacitas=40):
        super().__init__(rendszam, szin, marka, evjarat, utas_kapacitas)
        self.csomag_kapacitas = csomag_kapacitas


class Motor(Jarmu):
    def __init__(self, rendszam, szin, marka, evjarat, utas_kapacitas=2):
        super().__init__(rendszam, szin, marka, evjarat, utas_kapacitas)


elso = Auto("ABC-123", "kék", "Ford", evjarat="1994", csomag_kapacitas=30)  # ez új példány == new instance, amit a konstruktor (constructor) hoz létre
masodik = Auto("TST-111", "sárga", "Fiat", "2001", 4)  # ez új példány == new instance, amit a konstruktor (constructor) hoz létre
zsofi = Ember("zsófi", "1993-09-06", "Mária")
elso.utas_beszall(zsofi)  # <==> ekvivalens utas_beszall(elso)
print(elso.utasok[0].nev)

# andris = Ember(None, "1992-10-17", "ágnes"), ez nem megy
andris = Ember("andris", "1992-10-17", "ágnes")
elso.utas_beszall(andris)
elso.utas_lista()
masodik.utas_lista()
masodik.utas_kiszall(andris)
elso.utas_kiszall(andris)
elso.utas_lista()

print()
print("Jármű: {}".format(elso))
print("Első jármű csomag kapacitása: {}".format(elso.csomag_kapacitas))

csilla = Ember("Homonnay Csilla", "1993-03-11", "Rockenbauer Gabriella")
andris.hazasodik(csilla)
