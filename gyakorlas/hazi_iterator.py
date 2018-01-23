import numpy as np
import datetime
now = datetime.datetime.now()
mostani_ido = 21

# TODO: kávézó nyitva/zárva X
# TODO mielott barki bejon egy dolgozonak be kell jonni es ki kell nyitni X
# TODO ha nincs meg nyitva a kavazo, akkor a vendegeket el kell kuldeni X
# TODO: első dolgozó nyisson X
# TODO: nem lehet bejönni, amíg nincs nyitva X
# TODO: nem lehet vásárolni, ha nincs bent dolgozó X
# TODO: ha kimegy az utolsó dolgozó kimennek a vendégek és bezár az üzlet X
# TODO: rakodás


class Beszallito:
    def __init__(self, nev, termek={}):
        self.nev = nev
        self.termek = termek

    def kipakol(self):
        hozott_termek = {"udito": 12, "torta": 4, "kave": 20}
        for key in hozott_termek:
           yield (hozott_termek[key] * key)



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
        self.nyitva = False
        self.zarora = 20

    def bejon(self, szemely):
        if type(szemely) == Dolgozo:
            self.dolgozok.append(szemely)
        elif type(szemely) == Vendeg and len(self.dolgozok) > 0:
            self.vendegek.append(szemely)
        else:
            print("{} nem johet be, meg nem vagyunk nyitva".format(szemely))
        if len(self.dolgozok) > 0:
            print("{} bejött, ezért jelenleg {} személy ({}) tartozkodik az uzletben".format(szemely, len(self.vendegek) + len(self.dolgozok), self.vendegek + self.dolgozok))

    def nyitas(self, dolgozo):
        if len(self.dolgozok) > 0:
            print("{} bejott, az uzlet nyitva van".format(dolgozo))
        else:
            print("Az uzlet zarva van")

    def rendel(self, vendeg):
        if len(self.dolgozok) > 0:
            if vendeg in self.vendegek:  # leellenorzi, hogy egyaltalan benn van-e
                valasztott_termek = np.random.choice(list(self.termekek.keys()))

                if self.termekek[valasztott_termek] > 0:
                    if vendeg.penz >= valasztott_termek.ar:
                        vendeg.penz -= valasztott_termek.ar
                        self.termekek[valasztott_termek] -= 1
                        self.kassza += valasztott_termek.ar
                        print("{} nagyon élvezi a finom {}-t, {} forintért!".format(vendeg.nev, valasztott_termek.nev,
                                                                                valasztott_termek.ar))
                    else:
                        print("{}-nak/nek nincs elég pénze a vásárláshoz!".format(vendeg.nev))
                else:
                    print("A termék sajnos elfogyott!")
            else:
                raise ValueError("Nem rendelhet, nincs bent!")
        else:
            raise ValueError("Nem tud rendelni, nincs benn alkalmazott!")

    def kimegy(self, szemely):
        if type(szemely) == Vendeg and szemely in self.vendegek:
            self.vendegek.remove(szemely)
            print(" {} kiment az uzletbol".format(szemely))
        elif type(szemely) == Dolgozo and szemely in self.dolgozok:
            if len(self.dolgozok) > 1 or mostani_ido >= self.zarora:
                self.dolgozok.remove(szemely)
                print("{} kiment az uzletbol".format(szemely))
            elif len(self.dolgozok) == 1 or mostani_ido < self.zarora:
                print("{} nem mehet ki, munkaido alatt egy dolgozonak mindenkepp az uzletben kell tartozkodni".format(self.dolgozok))
        else:
            print("{} nem tartózkodik az üzletben!".format(szemely))

        if len(self.dolgozok) <= 0 and mostani_ido > self.zarora:
            print("Mivel minden dolgozo hazamegy a vendegeknek is el kell hagyniuk az uzletet")
            print("{} elhagyja/elhagyjak az uzletet".format(self.vendegek))
            self.vendegek = []
            #print("{} jelenleg {} személy ({}) tartozkodik az uzletben".format(szemely, len(self.vendegek) + len(self.dolgozok), self.vendegek + self.dolgozok))

    def bepakol(self, torta_be, udito_be, kave_be):
        pass




def main():
    sanyi = Dolgozo("Sanyi")
    anna = Dolgozo("Anna")
    jozsi = Vendeg("Jozsi", 600)
    noemi = Vendeg("Noemi", 200)

    torta = Termek("torta", 10)
    kave = Termek("kave", 20)
    udito = Termek("udito", 30)

    uzlet = Kavezo("Coffee", "1082, Só u. 2", "tfsz", {torta: 6, kave: 90, udito: 50}, 100000)
    kamilla = Vendeg("Kamilla", 2000)
    uzlet.bejon(sanyi)
    uzlet.nyitas(sanyi)
    uzlet.bejon(kamilla)
    uzlet.bejon(anna)
    uzlet.bejon(jozsi)
    uzlet.kimegy(anna)
    uzlet.kimegy(sanyi)

    uzlet.bejon(noemi)
    # uzlet.rendel(kamilla)
   # uzlet.rendel(jozsi)

    print(uzlet.vendegek)
    print(uzlet.kassza)

    csomagter = Beszallito("csomagter", {"torta": 65, "udito": 120, "kave": 25})
    x = csomagter.kipakol()
    for t in x:
        print(t)

    #uzlet.bepakol(5, 4, 3)

if __name__ == '__main__':
    main()
