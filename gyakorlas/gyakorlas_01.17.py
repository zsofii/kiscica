def utasok():
    yield 1
    yield 2
    yield 3

x = utasok()

for utas in x:
    print(utas)

x =utasok()
print(next(x))