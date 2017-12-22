from osztalyok.allat import Macska, Kutya
from osztalyok.ember import Ember

pali = Macska("Pali")
sajt = Macska("Sajt")

szamoca = Kutya("Szamóca")

andris = Ember("Vidosits András", "1992-10-17", "Nagy Ágnes", [pali, sajt, szamoca])

print(andris.hazi_allatok)
