from osztalyok.allat import Macska, Kutya, Allat
from osztalyok.ember import Ember

pali = Macska("Pali")
sajt = Macska("Sajt")

szamoca = Kutya("Szamóca")

balazs = Ember("Sajtos Balázs", "1992.10.17.", "Tóth Ágota", [pali, sajt, szamoca])
geza = Ember("Géza", "1999.10.17.", "Tóth Ágota", [pali, sajt, szamoca])
balazs + geza
balazs + geza
balazs - geza
balazs - geza
balazs + geza

print(balazs.hazi_allatok)

print(geza.kromoszoma_szam())

print(pali.fajnev())

tigris = Allat("tigris")


