# -*- coding: utf-8 -*-

class Jarmu:
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

