class Utaslista:
    def __init__(self, utasok):
        self.utasok = utasok

    def __len__(self):
        return len(self.utasok)


u = Utaslista(["zsófi", "csilla", "andris"])

print(len(u))

print("poz:")


# pozícionális paraméterek


def poz(a, b, c):
    print("a: {}, b: {}, c: {}".format(a, b, c))


poz(1, 2, 3)
poz(3, 2, 1)

print("kulcsszó")
# kulcsszó paraméterek

poz(c=3, b=1, a=2)

# opcionális

print("opcionalis")


def opcionalis(a, b, c=10):
    print("a: {}, b: {}, c: {}".format(a, b, c))


opcionalis(1, 2, 3)
opcionalis(3, 2)
opcionalis(c=3, b=1, a=2)
opcionalis(b=1, a=10)


# opcionalis 2
print("opcionalis 2")


# ezt nem lehet, opcionálisat nem követhet nem-opcionális
# def opcionalis2(a, b=10, c):
#   print("a: {}, b: {}, c: {}".format(a, b, c))


# nargs, kwargs

def csacskasag(elso_poz, masodik_poz, *pozicionalisak, a, b, **kulcsszavak):
    print("poz: {}".format(pozicionalisak))
    print("kulcs: {}".format(kulcsszavak))


csacskasag(10, 20, 30, "harcsa", 234, 123, 123, 123, 123, 12, 3, 123, 12, 3, a=5, b=6, c=7)


def osszeado(*nargs):
    osszeg = 0
    for szam in nargs:
        osszeg += szam
    return osszeg


print(osszeado(10, 20, 30, 2318218473274, 123123, 12312312,111, 111,1111))


print("A {alany} szereti a {szereti} es utálja a {utalja}".format(alany="kiskutya", szereti="húst", utalja="gyümölcsöt"))


virtualenv
