# -*- coding: utf-8 -*-


class Jarmu:
    def __init__(self, rendszam, szin, marka, evjarat, kapacitas=5):
        self.szin = szin
        self.marka = marka
        self.evjarat = evjarat
        self.kapacitas = kapacitas
        self.__utasok = []
        self.rendszam = rendszam

    @property
    def utasok(self):
        return self.__utasok

    @utasok.setter
    def utasok(self, value):
        self.__utasok = value

    @utasok.getter
    def utasok(self):
        return self.__utasok

    def utas_beszall(self, utas):
        if self.kapacitas > len(self.__utasok):
            self.__utasok.append(utas)
            print("Jelenleg {} utas tartozkódik a járműben!".format(len(self.__utasok)))

    def utas_kiszall(self, utas):
        if utas in self.__utasok:
            self.__utasok.remove(utas)
        else:
            print("{} nincs a {} utasai között!".format(utas, self))

    def utas_lista(self):
        print("A {} jármű utasai: {}".format(self.szin, self.__utasok))

    def __repr__(self):
        return self.rendszam


class Auto(Jarmu):
    def __init__(self, rendszam, szin, marka, evjarat, utas_kapacitas=4, csomag_kapacitas=40):
        super(Auto, self).__init__(rendszam, szin, marka, evjarat, utas_kapacitas)
        self.csomag_kapacitas = csomag_kapacitas


class Motor(Jarmu):
    def __init__(self, rendszam, szin, marka, evjarat, utas_kapacitas=2):
        super(Motor, self).__init__(rendszam, szin, marka, evjarat, utas_kapacitas)
