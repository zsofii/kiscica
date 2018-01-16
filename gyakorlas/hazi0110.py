import numpy as np


# TODO vásárló és eladó az ember osztályból örököljön x
# TODO ember osztályon belül fv-ek bejön kimegy vásárol
class Ember:
    def __init__(self, nev):
        if nev is not None:
            self.nev = nev

    def __repr__(self):
        return self.nev


class Dolgozo(Ember):
    def __init__(self, nev):
        super(Dolgozo, self).__init__(nev)
        self.nev = nev


# TODO vásárlók: név és hogy mennyi pénz van náluk
class Vendeg(Ember):
    def __init__(self, nev, penz):
        super(Vendeg, self).__init__(nev)
        self.nev = nev
        self.penz = penz


# TODO KÁVÉZÓ OSZTÁLY, VEZETNI BENNE, HOGY MENNYI PÉNZ VAN A PÉNZTÁRBAN x
# TODO rendel a készletből - 6 szelet torta, 90 kávé, 50 üdítő x
# TODO raktárkészlet dictionaryben legyen kulcs string mi , value hánydarab int x
# TODO minden tranzakciónál csökkeneteni kell a raktárkészletet az elfogyasztott dologgal
class Kavezo:
    def __init__(self, nev, cim, elerhetoseg, dolgozok, vendegek=[], kassza=0):
        self.nev = nev
        self.cim = cim
        self.elerhetoseg = elerhetoseg
        self.kassza = kassza
        self.dolgozok = dolgozok
        self.vendegek = vendegek
        self.termekek = {"torta": 6, "kave": 90, "udito": 50}

    def bejon(self, vendeg):
        self.vendegek.append(vendeg)
        print("{} bejött, ezért jelenleg {} tartozkodik az uzletben".format( vendeg, len(self.vendegek)))

    # TODO figyelni kell, hogy csak olyan ember vásárolhat, aki bejött
    # TODO véletlen szerűen választ valamit (Andris már megírta)
    # TODO a kiválasztott termék árát kifizeti
    def rendel(self, vendeg):
        termekek = ["kiscica", "kiskutya", "kisegér"]

        print(np.random.choice(termekek)) # választás véletlenszerűen a listából

    def kimegy(self, vendeg):
        self.vendegek.remove(vendeg)
        print(" {} kiment az uzletbol".format(vendeg))


# ide kell írni mindent, amit futtatni/példányosítani akarunk
def main():
    sanyi = Dolgozo("Sanyi")
    jozsi = Vendeg("jozsi", 1000)

    uzlet = Kavezo("Sanyi kavezoja", "1082, Corvin Sltány 2/E", "ez ugye egy telefonszám legyen nem?", [sanyi], [jozsi], 100000)
    kamilla = Vendeg("kamilla", 2000)
    uzlet.bejon(kamilla)

    print(jozsi.nev, jozsi.penz)


# ugye itt kezdődik a program, de ez egyből a main()-t hívja meg
if __name__ == '__main__':
    main()

# TODO vendegek read only properity
# @property
# def vendegek(self):
# nevek = []
# for vendeg in self.__vendegek:
#   nevek.append(vendeg.nev)
# return nevek

# @utasok.setter
# def vendegek(self, value):
# self.__vendegek = value


# def vasarol
# def kimegy
#        if utas in self.__utasok:
#           self.__utasok.remove(utas)


# TODO adott pillaantban hány vevő van a kávézóban
# TODO milyen termékeket rendelnek meg


# TODO minden terméknek lesz egy ára

# TODO vendégek mező -read only properity le lehessen kérdeni a nevüket, de mást ne lehessen megtdni
# TODO Kávézónak kell lenni konstruktorának - benne leyen a kávézó címe, telefonszáma, 2db eladó lista
