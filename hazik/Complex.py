import math


class Complex(object):
    _real = 0
    _imaginary = 0
    _magnitude = 0
    _phase = 0

    def real(self):
        return self._real

    def imaginary(self):
        return self._imaginary

    def magnitude(self):
        return self._magnitude

    def phase(self):
        return self._phase * (180 / math.pi)

    def __init__(self, real=0, imaginary=0):
        self.real = real
        self.imaginary = imaginary

    def __repr__(self):
        return "{}+{}j\t Magnitude: {:0.2f} \t Phase: {:0.2f}°".format(self._real, self._imaginary, self._magnitude, self._phase * (180 / math.pi))

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
