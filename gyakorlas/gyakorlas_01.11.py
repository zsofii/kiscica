from osztalyok.ember import Ember
from osztalyok.jarmu import Auto

kiskocsi = Auto(evjarat=2005, marka="Toyota", rendszam="IJK-789", szin="piros")

utas = Ember(nev="Tóth Alajos", anyja_neve="Rozsdás Éva", szuletesi_datum="1981.07.11.")

kiskocsi.utas_beszall(utas)

kiskocsi.__utasok.clear()

kiskocsi.utas_lista()
