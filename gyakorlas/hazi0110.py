import numpy as np


# TODO: kávézó nyitva/zárva
# TODO: első dolgozó nyisson
# TODO: nem lehet bejönni, amíg nincs nyitva
# TODO: nem lehet vásárolni, ha nincs bent dolgozó
# TODO: ha kimegy az utolsó dolgozó kimennek a vendégek és bezár az üzlet
# TODO: rakodás

class Termek:
    def __init__(self, nev, ar):
        self.nev = nev
        self.ar = ar

    def __repr__(self):
        return "{} ({}. ft)".format(self.nev, self.ar)


class Ember:
    def __init__(self, nev):
        if nev is not None:
            self.nev = nev

    def __repr__(self):
        return "{} ({})".format(self.nev, self.__class__.__name__)


class Dolgozo(Ember):
    def __init__(self, nev):
        super(Dolgozo, self).__init__(nev)
        self.nev = nev


class Vendeg(Ember):
    def __init__(self, nev, penz):
        super(Vendeg, self).__init__(nev)
        self.nev = nev
        self.penz = penz


class Kavezo:
    def __init__(self, nev, cim, elerhetoseg, termekek, kassza=0):
        self.nev = nev
        self.cim = cim
        self.elerhetoseg = elerhetoseg
        self.kassza = kassza
        self.dolgozok = []
        self.vendegek = []
        self.termekek = termekek

    def bejon(self, szemely):
        if type(szemely) == Vendeg:
            self.vendegek.append(szemely)
        elif type(szemely) == Dolgozo:
            self.dolgozok.append(szemely)

        print("{} bejött, ezért jelenleg {} személy ({}) tartozkodik az uzletben".format(szemely, len(self.vendegek) + len(self.dolgozok), self.vendegek + self.dolgozok))

    def rendel(self, vendeg):
        if vendeg in self.vendegek:  # leellenorzi, hogy egyaltalan benn van-e
            valasztott_termek = np.random.choice(list(self.termekek.keys()))

            if self.termekek[valasztott_termek] > 0:
                if vendeg.penz >= valasztott_termek.ar:
                    vendeg.penz -= valasztott_termek.ar
                    self.termekek[valasztott_termek] -= 1
                    self.kassza += valasztott_termek.ar
                    print("{} nagyon élvezi a finom {}-t, {} forintért!".format(vendeg.nev, valasztott_termek.nev, valasztott_termek.ar))
                else:
                    print("{}-nak/nek nincs elég pénze a vásárláshoz!".format(vendeg.nev))
            else:
                print("A termék sajnos elfogyott!")
        else:
            raise ValueError("Nem rendelhet, nincs bent!")

    def kimegy(self, szemely):
        if type(szemely) == Vendeg and szemely in self.vendegek:
            self.vendegek.remove(szemely)
            print(" {} kiment az uzletbol".format(szemely))
        elif type(szemely) == Dolgozo and szemely in self.dolgozok:
            self.dolgozok.remove(szemely)
            print(" {} kiment az uzletbol".format(szemely))
        else:
            print("{} nem tartózkodik az üzletben!".format(szemely))


def main():
    sanyi = Dolgozo("Sanyi")
    jozsi = Vendeg("jozsi", 600)

    torta = Termek("torta", 10)
    kave = Termek("kave", 20)
    udito = Termek("udito", 30)

    uzlet = Kavezo("Coffee", "1082, Só u. 2", "tfsz", {torta: 6, kave: 90, udito: 50}, 100000)
    kamilla = Vendeg("kamilla", 2000)
    uzlet.bejon(sanyi)
    uzlet.bejon(kamilla)
    uzlet.bejon(jozsi)
    uzlet.rendel(jozsi)
    uzlet.rendel(jozsi)
    uzlet.kimegy(kamilla)
    uzlet.kimegy(kamilla)

    print(uzlet.vendegek)
    print(uzlet.kassza)


if __name__ == '__main__':
    main()
