from osztalyok.ember import Ember

jozsi = Ember("jozsi", "1992-10-17", 25, "ágnes")
kata = Ember("kata", "1993-03-11", 24, "éva")
nora = Ember("nora", "1995-07-21", 22, "noemi")
andras = Ember("andras", "1993-07-07", 24, "anna")
timea = Ember("timea", "2000-02-02", 17, "amelia")
jonas = Ember("jonas", "1991-01-06", 27, "emma")
eszter =Ember("eszter", "1990-08-09", 27, "erzsebet")
norbert = Ember("norbert", "1989-10-10", 28, "annamaria")
adorjan = Ember ("adorjan", "1990-12-21", 27, "anna")
lilla = Ember("lilla", "1990-12-31", 27, "marta")

jozsi.hazasodik(kata)
jozsi.hazasodik(nora)
timea.hazasodik(andras)

jozsi.elvalik(nora)
jonas.elvalik(kata)

#print("Jozsi hazastars: {}".format(jozsi.hazastars))


norbert + eszter


print("Jozsi hazastars: {}".format(jozsi.hazastars))

# TODO: váljanak el, de csak akkor ha már összeházasodtak!!!

adorjan - lilla

#print("Jozsi hazastars: {}".format(jozsi.hazastars))
