from osztalyok.allat import Macska
from osztalyok.ember import Ember

pali = Macska("Pali")
sajt = Macska("Sajt")

andris = Ember("Vidosits András", "1992-10-17", "Nagy Ágnes", [pali, sajt])

print(andris.hazi_allatok)
