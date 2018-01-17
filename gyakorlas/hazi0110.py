import numpy as np

# TODO vásárló és eladó az ember osztályból örököljön x
# TODO vendegek read only properity
# TODO !!!!!!! vendégek mező -read only properity le lehessen kérdeni a nevüket, de mást ne lehessen megtdni
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


# TODO vásárlók: név és hogy mennyi pénz van náluk x
class Vendeg(Ember):
    def __init__(self, nev, penz):
        super(Vendeg, self).__init__(nev)
        self.nev = nev
        self.penz = penz

# TODO ember osztályon belül fv-ek bejön kimegy vásárol x
# TODO KÁVÉZÓ OSZTÁLY, VEZETNI BENNE, HOGY MENNYI PÉNZ VAN A PÉNZTÁRBAN x
# TODO rendel a készletből - 6 szelet torta, 90 kávé, 50 üdítő x
# TODO raktárkészlet dictionaryben legyen kulcs string mi , value hánydarab int x
# TODO !!!!!!!!! minden tranzakciónál csökkeneteni kell a raktárkészletet az elfogyasztott dologgal
# TODO Kávézónak kell lenni konstruktorának - benne leyen a kávézó címe, telefonszáma, 2db elad
# TODO adott pillaantban hány vevő van a kávézóban x


class Kavezo:
    def __init__(self, nev, cim, elerhetoseg,  termekek, dolgozok=[], vendegek=[], kassza=0,):
        self.nev = nev
        self.cim = cim
        self.elerhetoseg = elerhetoseg
        self.kassza = kassza
        self.dolgozok = dolgozok
        self.vendegek = vendegek  # lehet, hogy nem is kell
        self.termekek = termekek

        #print(self.termekek)
        #kaphato_aruk = termekek.keys()
        #print(kaphato_aruk)
        #aruk_ara = termekek.values()
        #print(aruk_ara)
        #mennyikave = termekek.get('kave')
        #print(mennyikave)
        #mennyikave = mennyikave - 1
        #print(mennyikave)

    def bejon(self, vendeg):
        self.vendegek.append(vendeg)
        print("{} bejött, ezért jelenleg {} tartozkodik az uzletben".format(vendeg, len(self.vendegek)))

    # TODO figyelni kell, hogy csak olyan ember vásárolhat, aki bejött x
    # TODO véletlen szerűen választ valamit (Andris már megírta) x
    # TODO a kiválasztott termék árát kifizeti x

    # TODO milyen termékeket rendelnek meg x
    # TODO minden terméknek lesz egy ára x
    def rendel(self, vendeg):
        if vendeg in self.vendegek:  # leellenorzi, hogy egyaltalan benn van-e
            kaphato_termekek = ["torta", "kave", "udito"]
            arak = [400, 300, 200]
            if vendeg.penz >= arak[2]:  # eloszures, hogy egyalatlan tud-e vasarolni
                valasztott_termek = np.random.choice(kaphato_termekek)
                print(valasztott_termek)
                if valasztott_termek == kaphato_termekek[1]:  # annak ellenorzese, hogy mit valaszt es azt meg tudja-e venni
                    if vendeg.penz >= arak[1]:  # itt hívtam volna meg a csökkentet
                        print("kavet valasztott")
                        vendeg.penz = vendeg.penz - arak[1]
                        print("{} forintja marad {} -nak:".format(vendeg.penz, vendeg))
                    else:
                        print("kerem valasszon valami mast {}".format(vendeg))
                elif valasztott_termek == kaphato_termekek[2]:
                    if vendeg.penz >= arak[2]:
                        print("uditot valasztott")
                        vendeg.penz = vendeg.penz - arak[2]
                        print ("{} forintja marad {} -nak:".format(vendeg.penz, vendeg))
                    else:
                        print("kerem valasszon valami mast {}".format(vendeg))
                else:
                    if vendeg.penz >= arak[0]:
                        print("tortat valasztott")
                        vendeg.penz = vendeg.penz - arak[0]
                        print("{} forintja marad {} -nak:".format(vendeg.penz, vendeg))
                    else:
                        print("kerem valasszon valami mast {}".format(vendeg))

            else:
                print("{} nem rendelkezik eleg fedezettel".format(vendeg))
        else:
            raise ValueError("Nem rendelhet, nincs bent!")

    def kimegy(self, vendeg):
        self.vendegek.remove(vendeg)
        print(" {} kiment az uzletbol".format(vendeg))

    def csokkent(self, termekek):
        if termekek == termekek[1]:
            mennyikave = termekek.get('kave')
            print(mennyikave)
            mennyikave = mennyikave - 1
            print(mennyikave)


# ide kell írni mindent, amit futtatni/példányosítani akarunk
def main():
    sanyi = Dolgozo("Sanyi")
    marcsi = Dolgozo("marcsi")
    jozsi = Vendeg("jozsi", 600)
    andrea = Vendeg("andrea", 4000)

    uzlet = Kavezo("Coffee", "1082, Só u. 2", "tfsz", {"torta": 6, "kave": 90, "udito": 50}, [sanyi], [jozsi], 100000,)
    kamilla = Vendeg("kamilla", 2000)
    uzlet.bejon(kamilla)
    #uzlet.bejon(jozsi)
    uzlet.rendel(jozsi)
    uzlet.rendel(jozsi)
    #uzlet.csokkent()



    #self.termekek[1]-=1

# ugye itt kezdődik a program, de ez egyből a main()-t hívja meg


if __name__ == '__main__':
    main()

#  print(np.random.choice(termekek)) # választás véletlenszerűen a listából