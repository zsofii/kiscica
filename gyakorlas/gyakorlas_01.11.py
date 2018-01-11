from osztalyok.ember import Ember
from osztalyok.jarmu import Auto

import numpy as np

kiskocsi = Auto(evjarat=2005, marka="Toyota", rendszam="IJK-789", szin="piros")

utas = Ember(nev="Tóth Alajos", anyja_neve="Rozsdás Éva", szuletesi_datum="1981.07.11.")

kiskocsi.utas_beszall(utas)

print(kiskocsi.utasok[0])

kiskocsi.utas_lista()


# véletlen választás

allatok = ["kiscica", "kiskutya", "kisegér"]

print(np.random.choice(allatok))
