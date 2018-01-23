import datetime
"""
igy lehet
tobb soros
kommentet irni
"""
myint = 5
print(type(myint))

print(ord("A"))  # how computers sees the letter A
print(ord("a"))

print(datetime.datetime.now())
print(str(datetime.datetime.now( ).date( )))


def Hello():
    print("This is my first function")

Hello()


def hello4(argCount, *varArgs):
    print("You passed ", argCount, " arguments.")
    for arg in varArgs:
        print(arg)



