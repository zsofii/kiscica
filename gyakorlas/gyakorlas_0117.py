def utasok():
    a = [1, 2, 3]
    for ertek in a:
        yield ertek
        yield ertek * 2


x = utasok()

for utas in x:
    print(utas)


def kipakol():
    hozott_termek = {"udito": 12, "torta": 4, "kave": 20, "harcsa": 50}
    for key in hozott_termek:
        yield key, hozott_termek[key]


for termek, darab in kipakol():
    print(termek, darab)
