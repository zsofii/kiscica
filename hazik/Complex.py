class Complex:
    def __init__(self, real=0, imaginary=0):
        self.real = real
        self.imaginary = imaginary

    def __repr__(self):
        return ""

    def __add__(self, other):
        # TODO: leellenőrizni, hogy az 'other' csak valós vagy egy másik complex szám lehessen
        # valós: type(other) == float


    # TODO: megírni a kivonás függvényt



def main():
    elso = Complex(10, 10)
    masodik = Complex(0, 2)

    print(elso)
    print(masodik)
    harmadik = elso + masodik
    print(harmadik)


if __name__ == "__main__":
    main()
