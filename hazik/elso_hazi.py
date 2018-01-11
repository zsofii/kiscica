# -*- coding: utf-8 -*-

from osztalyok.ember import Ember
from osztalyok.jarmu import Auto

elso = Auto("ABC-123", "kék", "Ford", evjarat="1994", csomag_kapacitas=30)  # ez új példány == new instance, amit a konstruktor (constructor) hoz létre
masodik = Auto("TST-111", "sárga", "Fiat", "2001", 4)  # ez új példány == new instance, amit a konstruktor (constructor) hoz létre
zsofi = Ember("zsófi", "1993-09-06", "Mária")
elso.utas_beszall(zsofi)  # <==> ekvivalens utas_beszall(elso)
print(elso.__utasok[0].nev)

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
