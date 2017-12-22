import math


class Complex:
    def __init__(self, real=0, imaginary=0):
        self.real = real
        self.imaginary = imaginary

    def __repr__(self):
        return ""

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)


def main():
    elso = Complex(10, 10)
    masodik = Complex(0, 2)

    print(elso)
    # masodik.phase = 45
    print(masodik)
    harmadik = elso + masodik
    print(harmadik)
    # harmadik -= masodik
    print(harmadik)


if __name__ == "__main__":
    main()
