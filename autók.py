# -*- coding: utf-8 -*-

class Ember(object):
    def __init__(self, nev, szuletesi_datum, anyja_neve):
        if nev is not None and szuletesi_datum is not None and anyja_neve is not None:
            self.nev = nev
            self.szuletesi_datum = szuletesi_datum
            self.anyja_neve = anyja_neve
        else:
            raise ValueError("A mezők kitöltése kötelező!")

    def __repr__(self):
        return self.nev

class Jarmu(object):
    def __init__(self, szin, marka, evjarat, kapacitas=5):
        self.szin = szin
        self.marka = marka
        self.evjarat = evjarat
        self.kapacitas = kapacitas
        self.utasok = []
        self.ajto = None


    def utas_beszall(self, utas):
        if self.kapacitas > len(self.utasok):
            self.utasok.append(utas)
            print("Jelenleg {} utas tartozkódik a járműben!".format(len(self.utasok)))
    
    def utas_lista(self):
        print("A {} jármű utasai: {}".format(self.szin, self.utasok))
    
    def __repr__(self):
        return "Szín: {}, Márka {}, Évjárat: {}, Kapacitás: {}, Utasok: {}".format(
        self.szin, self.marka, self.evjarat, self.kapacitas, self.utasok
    )

class Auto(Jarmu):
    def __init__(self, szin, marka, evjarat, utas_kapacitas=4, csomag_kapacitas=40):
        super().__init__(szin, marka, evjarat, utas_kapacitas)
        self.csomag_kapacitas = csomag_kapacitas
        



elso = Auto("kék", "Ford", evjarat="1994", csomag_kapacitas=30) # ez új példány == new instance, amit a konstruktor (constructor) hoz létre
masodik = Auto("sárga", "Fiat", "2001", 4) # ez új példány == new instance, amit a konstruktor (constructor) hoz létre
zsofi = Ember("zsófi", "1993-09-06", "Mária")
elso.utas_beszall(zsofi) # <==> ekvivalens utas_beszall(elso)
print(elso.utasok[0].nev)

# andris = Ember(None, "1992-10-17", "ágnes"), ez nem megy
andris = Ember("andris", "1992-10-17", "ágnes")
elso.utas_beszall(andris)

elso.utas_lista()
masodik.utas_lista()

print("Jármű: {}".format(elso))
print("Első jármű csomag kapacitása: {}".format(elso.csomag_kapacitas))
 