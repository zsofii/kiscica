import math


class Complex(object):
    _real = 0
    _imaginary = 0
    _magnitude = 0
    _phase = 0

    @property
    def real(self):
        return self._real

    @property
    def imaginary(self):
        return self._imaginary

    @property
    def magnitude(self):
        return self._magnitude

    @property
    def phase(self):
        return self._phase * (180 / math.pi)

    @real.setter
    def real(self, value):
        self._real = value
        self._magnitude = math.sqrt(
            math.pow(self._real, 2) + math.pow(self._imaginary, 2))
        self._phase = math.atan2(self._imaginary, self._real)

    @imaginary.setter
    def imaginary(self, value):
        self._imaginary = value
        self._magnitude = math.sqrt(
            math.pow(self._real, 2) + math.pow(self._imaginary, 2))
        self._phase = math.atan2(self._imaginary, self._real)

    @magnitude.setter
    def magnitude(self, value):
        self._magnitude = value
        self._real = self._magnitude * math.cos(self._phase)
        self._imaginary = self._magnitude * math.sin(self._phase)

    @phase.setter
    def phase(self, value):
        self._phase = value * (math.pi / 180)
        self._real = self._magnitude * math.cos(self._phase)
        self._imaginary = self._magnitude * math.sin(self._phase)

    def __init__(self, real=0, imaginary=0):
        self.real = real
        self.imaginary = imaginary

    def __repr__(self):
        return "{}+{}j\t Magnitude: {:0.2f} \t Phase: {:0.2f}°".format(self._real, self._imaginary, self._magnitude, self._phase * (180 / math.pi))

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imaginary - other.imaginary)


def main():
    elso = Complex(10, 10)
    masodik = Complex(0, 2)

    print(elso)
    # masodik.phase = 45
    print(masodik)
    harmadik = elso + masodik
    print(harmadik)
    harmadik -= masodik
    print(harmadik)


if __name__ == "__main__":
    main()
