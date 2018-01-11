from osztalyok.allat import Macska, Kutya
from osztalyok.ember import Ember

pali = Macska("Pali")
sajt = Macska("Sajt")

szamoca = Kutya("Szamóca")

balazs = Ember("Sajtos Balázs", "1992.10.17.", "Tóth Ágota", [pali, sajt, szamoca])
geza = Ember("Géza", "1999.10.17.", "Tóth Ágota", [pali, sajt, szamoca])
balazs + geza

print(balazs.hazi_allatok)
