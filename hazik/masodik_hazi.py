from osztalyok.ember import Ember

jozsi = Ember("jozsi", "1992-10-17", "ágnes")
kata = Ember("kata", "1993-03-11", "éva")
jozsi.hazasodik(kata)

print("Jozsi hazastars: {}".format(jozsi.hazastars))

jozsi + kata

print("Jozsi hazastars: {}".format(jozsi.hazastars))

# TODO: váljanak el, de csak akkor ha már összeházasodtak!!!

jozsi - kata

print("Jozsi hazastars: {}".format(jozsi.hazastars))
